import socket

conn= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverip = "16.189.29.54"
port = 8080
conn.bind((serverip, port))
conn.listen(5)
(client, addr) = conn.accept()

print "Connection Established\n"

client.close()
conn.close
