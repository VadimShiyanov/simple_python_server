import socket
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.connect(('localhost', 9339))
t = input("Enter text message \n")
srv.sendall(t.encode('utf-8'))
data = srv.recv(1024)
srv.close()