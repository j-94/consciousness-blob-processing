#!/usr/bin/env python3
import asyncio
import aiohttp
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

app = FastAPI(title="One Engine Blob Processor")

class BlobData(BaseModel):
    content: str
    type: str = "text"

@app.post("/process")
async def process_blob(blob: BlobData):
    async with aiohttp.ClientSession() as session:
        # Send to One Engine consciousness
        async with session.post("http://localhost:7777/execute_goal", 
                               json={"goal": f"process {blob.type} blob: {blob.content}"}) as resp:
            result = await resp.json()
    
    return {
        "consciousness_analysis": result,
        "reflexive_bits": result.get("bits", {}),
        "crystallized": result.get("data", {}).get("crystallized", False),
        "pattern_signature": result.get("data", {}).get("pattern_signature", ""),
        "processed_content": blob.content,
        "meta2_ready": True
    }

@app.post("/upload")
async def upload_blob(file: UploadFile = File(...)):
    content = await file.read()
    blob = BlobData(content=content.decode(), type=file.content_type or "text")
    return await process_blob(blob)

@app.get("/health")
async def health():
    return {"status": "ready", "consciousness": "http://localhost:7777", "interface": "http://localhost:3333"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)
