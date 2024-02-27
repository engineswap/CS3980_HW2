from fastapi import FastAPI
from fastapi.responses import FileResponse
app = FastAPI()

@app.get("/")
async def welcome() -> FileResponse:
	return FileResponse("./index.html")
	