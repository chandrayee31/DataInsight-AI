def build_insight_prompt(summary: dict) -> str:
    prompt = f"""
You are a business data analyst.

Analyze the following dataset summary and produce a clear, business-friendly report.

Dataset Summary:
- Total rows: {summary['total_rows']}
- Total columns: {summary['total_columns']}
- Total sales: {summary['total_sales']:.2f}
- Total profit: {summary['total_profit']:.2f}
- Total quantity sold: {summary['total_quantity']}

Top 3 regions by sales:
{summary['top_region_sales']}

Category-wise sales:
{summary['top_category_sales']}

Category-wise profit:
{summary['profit_by_category']}

Please provide the output in exactly these sections:
1. Executive Summary
2. Key Observations
3. Business Risks or Anomalies
4. Recommendations

Keep the language concise, professional, and easy for business stakeholders to understand.
Do not invent facts outside the provided summary.
"""
    return prompt