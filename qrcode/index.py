from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from fastapi.responses import FileResponse

import qrcode

class File_QR(BaseModel):
    name: str

app = FastAPI()

@app.get("/")
def hello():
    return {"hello": "world"}

@app.post("/")
def create_qr(item: File_QR):
    try:
        img = qrcode.make(item.name)
        type(img)

        path_image = "results/image.png"

        file_save = img.save(path_image)

        # create download link
        download_image = FileResponse(
            path=path_image,
            filename=path_image,
            media_type='image/png'
        )

        return download_image

        # return {
        #     "response" : "successfully create qr",
        #     "image": download_image
        # }
    except:
        return{
            "cannot process data"
        }

