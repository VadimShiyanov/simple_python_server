import socket

# Create a socket object using IPv4 and TCP
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the specified address ('localhost') and port (9339)
srv.bind(('localhost', 9339))

# Listen for incoming connections with a backlog of 1
srv.listen(1)

# Accept an incoming connection, creating a new socket (connection) for communication
connection, address = srv.accept()

# Continuous loop for receiving and sending data
while True:
    # Receive data (up to 1024 bytes) from the client
    data = connection.recv(1024)

    # Break the loop if no data is received
    if not data:
        break

    # Send the received data back to the client
    connection.sendall(data)

    # Decode the received data as UTF-8
    data = data.decode('utf-8')

    # Open a text file ('text.txt') in write mode and write the decoded data
    with open('text.txt', "w") as file:
        file.write(data + "\n")

    # Open the text file in read mode and print its content line by line
    with open('text.txt', "r") as read_file:
        for n in read_file:
            print(n, end="")

# Close the file and the connection
connection.close()
