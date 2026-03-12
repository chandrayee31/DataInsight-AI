# DataInsight AI

AI-powered dataset insight generator built with FastAPI, pandas, and Ollama.

## Overview
DataInsight AI accepts a CSV dataset, performs automated exploratory data analysis (EDA), and generates business-friendly insights using a locally hosted LLM.

## Features
- CSV upload and validation
- Automated dataset summary
- Sales, profit, quantity, and category analysis
- LLM-generated executive summary and recommendations
- FastAPI REST API
- Docker support
- Structured JSON responses

## Tech Stack
- Python
- FastAPI
- pandas
- Ollama
- Pydantic
- Docker

## Project Structure
```text
app/
data/
tests/
Dockerfile
requirements.txt
README.md