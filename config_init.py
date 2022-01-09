from configparser import ConfigParser
from glob import glob

def ini_config():
    config=ConfigParser()
    config.read(glob("*.ini"))
    ip_conf=variables(
            config["host"]["ip"], 
            int(config["host"]["port"]), 
            config['base']['base'],
            config['table']['table_pc'],
            config['table']['table_prog'])    
    return ip_conf

class variables:
    def __init__(self,ip,port, base, table_pc, table_prog):
        self.ip=ip
        self.port=port
        self.base=base
        self.table_pc=table_pc
        self.table_prog=table_prog

cfg=ini_config()
ip=cfg.ip
port=cfg.port
base=cfg.base
table_pc=cfg.table_pc
table_prog=cfg.table_prog
