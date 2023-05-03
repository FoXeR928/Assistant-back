from configparser import ConfigParser
from glob import glob

def ini_config():
    config=ConfigParser()
    config.read(glob("*.ini"))
    ip_conf=variables(
            config["host"]["ip"], 
            int(config["ports"]["port_app"]),
            int(config["ports"]["port_socket"]),
            config['base']['base'],
            config['table']['table_users'],
            config['table']['table_pc'],
            config['table']['table_prog'])    
    return ip_conf

class variables:
    def __init__(self,ip, port_app, port_socket, base, table_users, table_pc, table_prog):
        self.ip=ip
        self.port_app=port_app
        self.port_socket=port_socket
        self.base=base
        self.table_users=table_users
        self.table_pc=table_pc
        self.table_prog=table_prog

cfg=ini_config()
ip=cfg.ip
port_app=cfg.port_app
port_socket=cfg.port_socket
base=cfg.base
table_users=cfg.table_users
table_pc=cfg.table_pc
table_prog=cfg.table_prog
