import socket

# Create a socket object using IPv4 and TCP
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server at the specified address and port
srv.connect(('localhost', 9339))

# Get input from the user to send as a text message
t = input("Enter text message \n")

# Encode the text message in UTF-8 and send it to the server
srv.sendall(t.encode('utf-8'))

# Receive data (up to 1024 bytes) from the server
data = srv.recv(1024)

# Close the socket connection
srv.close()
