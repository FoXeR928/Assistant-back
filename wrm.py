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

start_programm('D:\Steam\Steam.exe','192.168.88.244', 'Asus-Pro-Gaming','')