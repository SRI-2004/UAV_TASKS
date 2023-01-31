import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 12345

s.connect((host, port))

msg = s.recv(1024)

print("Received message:", msg.decode("utf-8"))

s.close()