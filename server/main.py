import base64
import os
import asyncio


import cv2
import numpy as np
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.status import HTTP_404_NOT_FOUND
from fastapi.responses import FileResponse,JSONResponse,HTMLResponse,PlainTextResponse


from exceptionhandler import default_http_exception_handler
from middleware import TimeoutMiddleware
from face import analyse_emotion

app = FastAPI()

app.add_exception_handler(StarletteHTTPException, default_http_exception_handler)
app.add_middleware(TimeoutMiddleware, timeout=5)

@app.get("/")
async def root():
    return FileResponse("./page/video.html")

resoure_dic = './res/'
@app.get("/res/{file_name}")
async def res(file_name: str):
    path = os.path.join(resoure_dic, file_name)
    if not os.path.isfile(path):
        raise StarletteHTTPException(status_code=HTTP_404_NOT_FOUND)
    return FileResponse(path)

class Image(BaseModel):
    data: str

@app.put("/face/emotion")
async def face_emotion(body: Image):
    img = base64.b64decode(body.data.encode("utf-8"))
    img = np.frombuffer(img, dtype = np.uint8)
    img = cv2.imdecode(np.array(img), flags=cv2.IMREAD_COLOR)
    data = analyse_emotion(img)
    if(data):
        ret = {'succeded': True, 'data': data}
    else:
        ret = {'succeded': False, 'data': data}
    return JSONResponse(ret)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app, port=5000, log_level="info")