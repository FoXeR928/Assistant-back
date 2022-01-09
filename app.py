import fastapi
from wake_on_lan import wake_pc
from sql import pc_mac

app = fastapi.FastAPI()

@app.post("/add_prog", status_code=fastapi.status.HTTP_201_CREATED)
def add_prog(path: str, programm:str):
    pass

@app.get("/wake_pc", status_code=fastapi.status.HTTP_201_CREATED)
def wake_pc_block():
    wake_pc(pc_mac)