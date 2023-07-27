import socket

HOST = "127.0.1.1"
PORT = 3000
ADDR = (HOST , PORT)
client = socket.socket(socket.AF_INET , socket.SOCK_STREAM) 
client.connect(ADDR)
print("type 'quit/q' to quit")
while True :
    msg = input(" -> ")
    if msg == "q" or msg == "quit"  :
        break 
    message = msg.encode("utf-8")
    client.send(message)
    data = client.recv(1024).decode("utf-8")
    print(data)


client.send(("CLOSE").encode("utf-8"))