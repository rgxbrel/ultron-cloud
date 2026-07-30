from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import os

app = FastAPI()

@app.get("/ping", response_class=PlainTextResponse)
@app.head("/ping")
async def ping():
    return "ok"

@app.get("/telegram/webhook", response_class=PlainTextResponse)
@app.post("/telegram/webhook")
async def telegram_webhook(request: Request):
    if request.method == "GET":
        return "ok"
    try:
        body = await request.json()
        update = body.get("update_id")
        message = body.get("message") or body.get("edited_message")
        if not message:
            return PlainTextResponse("ok", status_code=200)

        chat_id = message.get("chat", {}).get("id")
        text = message.get("text") or ""
        if chat_id is None:
            return PlainTextResponse("ok", status_code=200)

        return PlainTextResponse("ok", status_code=200)
    except Exception:
        return PlainTextResponse("error", status_code=500)

@app.get("/", response_class=PlainTextResponse)
@app.head("/")
async def root():
    return "ok"
