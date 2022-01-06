import winrm
from config_init import win

session=winrm.Session(win)
session.run_cmd('shutdown')