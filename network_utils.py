import socket

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        s.connect(('8.8.8.8', 80))
        
        local_ip = s.getsockname()[0]
        
        s.close()
        
        return local_ip
    except socket.error as e:
        print(f"Erro ao obter o endereço IP: {e}")
        return None

local_ip = get_local_ip()
if local_ip:
    print(f"Endereço IP local: {local_ip}")
else:
    print("Não foi possível obter o endereço IP local.")
