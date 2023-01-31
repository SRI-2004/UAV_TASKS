import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)

print("Server listening on port", port)

conn, addr = s.accept()

print("Got connection from", addr)

conn.send(b"Hello, client!")
conn.close()
