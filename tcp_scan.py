import socket

def scan_ports(host, port_list):
    for port in port_list:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        sock.close()

if __name__ == '__main__':
    host = input("Enter the host to be scanned: ")
    ports = input("Enter the ports to be scanned separated by commas: ")
    port_list = [int(port) for port in ports.split(',')]
    scan_ports(host, port_list)
