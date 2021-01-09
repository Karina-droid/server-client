import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 5000))
    while True:
        to_server = input()
        s.sendall(to_server.encode('utf-8'))
        from_server = s.recv(1024)
        print('Server: ', repr(from_server.decode('utf-8')))