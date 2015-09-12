import re

# You are working on an SSH client and need an auxiliary function that determines whether a given string, such as "127.12.23.43:5000", represents a valid socket address.
#
# A valid socket address has the format x.y.z.w:port, where x, y, z, w are integers ranging from 0 and 255, inclusive, and port is an integer ranging from 1 to 65,535, inclusive. For example, the string "127.12.23.43:5000" is a valid socket address, while the string "127.A:-12" is not.

def is_valid_socket(socket_addr):
    #I chose not to declare this false if the port number begins with numerous 0s, 
    #because that wasn't explicitly instructed.
    try:
        socket_addr_list = socket_addr.split(":")
        ip_addr_list = socket_addr_list[0].split(".")
        port_address = int(socket_addr_list[1])
    except:
        return False
    
    try:
        for byte_addr in ip_addr_list:
            byte_addr_int = int(byte_addr)
            if byte_addr_int < 0 or byte_addr_int > 255:            
                return False
            else:
                continue
    except:
        return False
    
    
    ip_address = bool(re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",socket_addr_list[0]))
    if (ip_address == True):
        if 1 <= port_address <= 65535:
            return True
        else:
            return False
    else:
        return False

