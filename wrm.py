import winrm
from config_init import win

session=winrm.Session(win)

def shutdown(time):
    session.run_cmd('shutdown '+time)