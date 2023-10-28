#fastapi html server

import uvicorn
import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

class MyModel(BaseModel):
    my_field: str = Field(..., alias="my_field_alias")
app = FastAPI()

app.mount("/fiel", StaticFiles(directory="fiel"), name="fiel")



#return html file in fiel folder
@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return FileResponse("fiel/index.html")

#serve static files in fiel folder
@app.get("/{file_path:path}")
async def read_file(file_path: str):
    return FileResponse("fiel/"+file_path)




if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)