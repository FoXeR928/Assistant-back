import winrm

def init_winrm(win, name, password):
    session=winrm.Session(win, auth=(name, password))
    return session

def shutdown(time, win, name, password):
    session=init_winrm(win, name, password)
    session.run_cmd('shutdown '+time)

def start_programm(path, win, name, password):
    session=init_winrm(win, name, password)
    session.run_cmd('start '+path)
