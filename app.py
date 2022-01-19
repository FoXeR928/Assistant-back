import fastapi
from bd_set import PC, PROG
from wake_on_lan import wake_pc
from wrm import shutdown, start_programm
from sql import read_mac, read_path, read_win

app = fastapi.FastAPI()

@app.post("/start_prog", status_code=fastapi.status.HTTP_201_CREATED)
def start_prog(programm:str, password: str):
    path=read_path(programm, PROG)
    win=read_win(password, PC)
    start_programm(path, win[0], win[1])

@app.get("/wake_pc", status_code=fastapi.status.HTTP_201_CREATED)
def wake_pc_block(password: str):
    pc_mac=read_mac(password, PC)
    wake_pc(pc_mac)

@app.get("/off_pc", status_code=fastapi.status.HTTP_201_CREATED)
def off_pc_block(time: str):
    shutdown(time)