# app.py

from fastapi import FastAPI
import time
import asyncio
from datetime import datetime

app = FastAPI()


@app.get("/blocking")
def blocking_endpoint():
    print(f"[{datetime.now()}] Blocking request started")

    # Blocks the worker thread for 5 seconds
    time.sleep(5)

    print(f"[{datetime.now()}] Blocking request finished")

    return {
        "endpoint": "blocking",
        "message": "Finished after 5 seconds"
    }


@app.get("/non-blocking")
async def non_blocking_endpoint():
    print(f"[{datetime.now()}] Non-blocking request started")

    # Releases control back to the event loop
    await asyncio.sleep(5)

    print(f"[{datetime.now()}] Non-blocking request finished")

    return {
        "endpoint": "non-blocking",
        "message": "Finished after 5 seconds"
    }


@app.get("/")
async def home():
    return {
        "message": "Visit /blocking or /non-blocking"
    }