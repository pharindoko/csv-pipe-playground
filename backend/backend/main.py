from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import errno
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    os.makedirs("files")
except OSError as exc: # Guard against race condition
    if exc.errno != errno.EEXIST:
        raise
@app.get("/")
async def hello_world():
    return {"hello": "world"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    if (file.filename.endswith('.csv')):
        file_location = f"files/{file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())
        return {"filename": file.filename}
    else:
        raise HTTPException(status_code=400, detail=f"{file.filename} is no csv file")
