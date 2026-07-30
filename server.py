from fastapi import FastAPI
from fastapi.responses import JSONResponse
import httpx
import os

app = FastAPI()
HERMES_BASE = os.getenv("HERMES_BASE", "http://127.0.0.1:9119")

@app.get("/ping")
async def ping():
    return {"status": "ok"}

@app.get("/health")
async def health():
    async with httpx.AsyncClient(timeout=10) as client:
        try:
            r = await client.get(f"{HERMES_BASE}/")
            return {"status": "ok", "hermes_status": r.status_code}
        except Exception as e:
            return JSONResponse(status_code=500, content={"status": "error", "detail": str(e)})
