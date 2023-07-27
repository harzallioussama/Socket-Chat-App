import socket 
import threading

HOST = socket.gethostbyname(socket.gethostname()) # your ip addr
PORT = 3000
ADDR = (HOST , PORT)
FORMAT = "utf-8"
CLOSE = "quit"

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(ADDR) 

clients = set() 
client_lock = threading.Lock() # to prevent race conditions

def request_handler(conn , addr) :
    try :
        # connection = True
        while True :
            # print(clients)
            data = conn.recv(1024).decode(FORMAT)
            if data == CLOSE :
                break 
            if data :
                print(f"[{addr}] : {data}")
                with client_lock :
                    for e in clients :
                        # if e != conn :
                        e.sendall((f"[{addr}] : {data}").encode(FORMAT))
                        # print(data)
    finally :
        with client_lock :
            clients.remove(conn)
        conn.close()
def start() :
    server.listen()
    while True :
        conn , addr  = server.accept()
        print(f"Connected by {addr}")
        with client_lock :
            clients.add(conn) 
        thread = threading.Thread(target = request_handler , args=(conn , addr))  
        thread.start() 
start()