from wakeonlan import send_magic_packet

def wake_pc(mac):
    try:
        send_magic_packet(mac)
        result={"error":0, "result":"Start PC"}
    except Exception as err:
        result={"error":1, "result":err}
    return result