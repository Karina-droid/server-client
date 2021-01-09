import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 5000))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by ", addr)
        while True:
            from_client = conn.recv(1024)
            if not from_client:
                break
            print("Cliet: ", from_client.decode('utf-8'))
            to_client = input()
            conn.sendall(to_client.encode('utf-8'))