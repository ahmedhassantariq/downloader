from fastapi import FastAPI
import json
import yt_dlp
from urllib.parse import unquote

app = FastAPI()

@app.get("/", tags=["Root"])
async def hello():
    return {"message":"Hello. How are you?"}

@app.get("/api/getVideoInfo/",)
async def downloader(url: str):
    ydl_opts = {}
    decoded_url = unquote(url)

    print(decoded_url)
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(decoded_url, download=False)
    return {json.dumps(ydl.sanitize_info(info))}
