from fastapi import FastAPI, UploadFile, File, HTTPException
import os
import tempfile
from app.utils.logger import logger

from app.services.analysis_service import load_and_validate_csv, generate_basic_summary
from app.services.prompt_service import build_insight_prompt
from app.services.llm_service import generate_insights
from app.models.response_models import AnalyzeResponse

app = FastAPI(title="DataInsight AI")


@app.get("/health")
def health_check():
    logger.info("Health check endpoint called")
    return {"status": "ok"}


@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze_file(file: UploadFile = File(...)):
    logger.info(f"Received file for analysis: {file.filename}")

    if not file.filename.endswith(".csv"):
        logger.error("Invalid file type uploaded")
        raise HTTPException(status_code=400, detail="Only CSV files are supported.")

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:
            temp_file.write(await file.read())
            temp_path = temp_file.name

        logger.info("File saved temporarily")
        df = load_and_validate_csv(temp_path)
        logger.info("CSV validated successfully")

        summary = generate_basic_summary(df)
        logger.info("Basic summary generated")

        prompt = build_insight_prompt(summary)
        logger.info("Prompt built successfully")

        insights = generate_insights(prompt)
        logger.info("Insights generated from Ollama")

        return AnalyzeResponse(summary=summary, insights=insights)

    except Exception as e:
        logger.exception("Error occurred during analysis")
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if "temp_path" in locals() and os.path.exists(temp_path):
            os.remove(temp_path)
            logger.info("Temporary file removed")