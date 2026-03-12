import pandas as pd

REQUIRED_COLUMNS = [
    "Order Date",
    "Region",
    "Category",
    "Sub-Category",
    "Sales",
    "Quantity",
    "Profit",
    "Segment",
]

def load_and_validate_csv(file_path:str)->pd.DataFrame:
    df = pd.read_csv(file_path, encoding="latin1")
    missing_col=[col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_col:
          raise ValueError(f"Missing required Columns:{missing_col}")
    df["Order Date"]=pd.to_datetime( df["Order Date"], errors="coerce")
    numeric_cols = ["Sales", "Quantity", "Profit"]
    for col in numeric_cols:
         df[col]=pd.to_numeric(df[col], errors="coerce")
    df=df.dropna(subset=["Order Date","Sales","Quantity","Profit"])
    return df

def generate_basic_summary(df:pd.DataFrame)-> dict:
    summary={}
    summary["total_rows"]=len(df)
    summary["total_columns"]=len(df.columns)
    summary["total_sales"] = float(df["Sales"].sum())
    summary["total_profit"] = float(df["Profit"].sum())
    summary["total_quantity"] = int(df["Quantity"].sum())
    summary["top_region_sales"] = (df.groupby("Region")["Sales"].sum().sort_values(ascending=False).head(3).to_dict())
    summary["top_category_sales"] = (df.groupby("Category")["Sales"].sum().sort_values(ascending=False).head(3).to_dict())
    summary["profit_by_category"] = (df.groupby("Category")["Profit"].sum().to_dict())

    return summary
