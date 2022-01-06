import configparser
import glob

def ini_config():
    config=configparser.ConfigParser()
    config.read(glob.glob("*.ini"))
    ip_conf=config["host"]["ip"], int(config["host"]["port"])    
    return ip_conf

class variables:
    def ip_init(self, ip, port):
        self.ip=ip
        self.port=port

cfg=ini_config()
print(cfg)
