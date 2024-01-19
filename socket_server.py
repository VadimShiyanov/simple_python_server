import socket
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind(('localhost', 9339))
srv.listen(1)
connection, addres = srv.accept()
while True:
    data = connection.recv(1024)
    if not data:
        break
    connection.sendall(data)
    data = data.decode('utf-8')
    file = open('text.txt', "w")
    file.write(data + "\n")
    file = open('text.txt', "r")
    for n in file:
        print(n, end = "")
    file.close
connection.close()