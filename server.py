from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import httpx
import os

app = FastAPI()
HERMES_BASE = os.getenv("HERMES_BASE", "http://127.0.0.1:9119")

@app.get("/ping", response_class=PlainTextResponse)
@app.head("/ping")
async def ping():
    return "ok"

@app.get("/health", response_class=PlainTextResponse)
@app.head("/health")
async def health():
    async with httpx.AsyncClient(timeout=10) as client:
        try:
            await client.get(f"{HERMES_BASE}/")
            return "ok"
        except Exception:
            return "error", 500

@app.get("/")
async def root():
    return {"status": "ok"}
