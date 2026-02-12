from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import akshare as ak
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/stock/{code}")
def get_stock(code: str):
    try:
        df = ak.stock_zh_a_hist(symbol=code, period="daily", adjust="")
        df = df.tail(100)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}
