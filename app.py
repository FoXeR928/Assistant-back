import fastapi
from bd_set import PC, PROG, USERS
from wake_on_lan import wake_pc
from sql import read_mac, read_path, read_win, write_path, write_pc

app = fastapi.FastAPI()

def check_result(check):
    if check["error"] == 1:
        message = {check["result"]}
        return {"error":1, "message": message}
    elif check["error"] == 0:
        message = check["result"]
        return {"error":0, "message": message}

def check_result_win(check):
    if check["error"] == 1:
        message = check["result"]
        return {"error":1, "message": message}
    elif check["error"] == 0:
        host = check["host"]
        pc_name=check["pc_name"]
        password=check["password"]
        return {"error":0, "host": host, "pc_name":pc_name, "password":password}

@app.post("/add_prog", status_code=fastapi.status.HTTP_201_CREATED)
def add_prog(user: str, pc: str,programm:str, path:str):
    check=write_path(user, pc,programm, path, PROG, USERS)
    result=check_result(check)
    return result

@app.post("/add_pc", status_code=fastapi.status.HTTP_201_CREATED)
def add_pc(user: str,host:str, mac: str, pc_name:str, password:str):
    check=write_pc(user, host, mac, pc_name, password, PC, USERS)
    result=check_result(check)
    return result

@app.get("/wake_pc", status_code=fastapi.status.HTTP_200_OK)
def wake_pc_block(user: str):
    pc_mac=read_mac(user, PC)
    result_first=check_result(pc_mac)
    check=wake_pc(result_first)
    result=check_result(check)
    print(pc_mac)
    return result