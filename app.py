import fastapi
from bd_set import PC, PROG
from wake_on_lan import wake_pc
from wrm import start_programm
from sql import read_mac, read_path

app = fastapi.FastAPI()

@app.post("/start_prog", status_code=fastapi.status.HTTP_201_CREATED)
def start_prog(programm:str):
    path=read_path(programm, PROG)
    start_programm(path)

@app.get("/wake_pc", status_code=fastapi.status.HTTP_201_CREATED)
def wake_pc_block(password: str):
    pc_mac=read_mac(password, PC)
    wake_pc(pc_mac)