import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Reserve a port for your service
port = 12345

# Connect the socket to the server
s.connect((host, port))

# Receive the message from the server
msg = s.recv(1024)

print("Received message:", msg.decode("utf-8"))

# Close the connection
s.close()