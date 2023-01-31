import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Reserve a port for your service
port = 12345

# Bind the socket to a specific address and port
s.bind((host, port))

# Listen for incoming connections
s.listen(5)

print("Server listening on port", port)

# Wait for a client to connect
conn, addr = s.accept()

print("Got connection from", addr)

# Send a message to the client
conn.send(b"Hello, client!")

# Close the connection
conn.close()
