from fastapi import FastAPI,UploadFile,File
from fastapi.middleware.cors import CORSMiddleware
from analyzer import gemini_analyzer
import asyncio
app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET","POST","OPTIONS"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"Status":"Soil Detector Running"}

@app.post("/check")
async def check(file: UploadFile=File(...)):
    image_bytes= await file.read()

    result= gemini_analyzer(image_bytes)

    return{"allow_seeding":result}