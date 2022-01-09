from wakeonlan import send_magic_packet

def wake_pc(mac):
    send_magic_packet(mac)