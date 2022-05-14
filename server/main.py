import base64


import cv2
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import FileResponse, JSONResponse, HTMLResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles


from exceptionhandler import default_http_exception_handler
from middleware import TimeoutMiddleware
from face import analyse_emotion


app = FastAPI()

app.add_exception_handler(StarletteHTTPException,
                          default_http_exception_handler)
app.add_middleware(TimeoutMiddleware, timeout=5)


@app.get("/")
async def root():
    return FileResponse("./page/video.html")

app.mount('/res', StaticFiles(directory="./res"))


class Image(BaseModel):
    data: str


@app.put("/face/emotion")
async def face_emotion(body: Image, getimg: Optional[bool] = False):
    img = base64.b64decode(body.data.encode("utf-8"))
    
    img = np.frombuffer(img, dtype=np.uint8)
    img = cv2.imdecode(img, flags=cv2.IMREAD_COLOR)
    ret = analyse_emotion(img)

    if(ret):
        data, img = ret
        ret = {'succeded': True, 'data': data}

    else:
        ret = {'succeded': False, 'data': ''}

    if(getimg):
        _, encodedimg = cv2.imencode(
            '.jpg', img, (cv2.IMWRITE_JPEG_QUALITY, 30))
        encodedimg = base64.b64encode(encodedimg)
        ret['img'] = encodedimg.decode("utf-8")

    return JSONResponse(ret)


@app.get("/game/")
async def face_emotion():
    return FileResponse('./game/index.html')

app.mount('/game/res', StaticFiles(directory="./game"), name='game')


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app, port=5000, log_level="info")
