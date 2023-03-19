import socket
import threading

HEADER = 1024
PORT = 5050
SERVER = 'localhost'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

Image_Array = []

def handle_test(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg = conn.recv(HEADER).decode(FORMAT)
        if 'CONN' in str(msg):
            print(msg)
            conn.sendall(b'CONNECTED')
        elif 'SEND' in str(msg):
            # Do the initialization action
            print(msg)
            conn.sendall(b'RECIEVED')
            Image_Array.append(msg)
            #print(Image_Array)
        elif 'QUIT' in str(msg):
            # Do the quiting action
            print(msg)
            conn.sendall(b'DISCONNECTED')
            break
    #conn.send("Msg received".encode(FORMAT))
    conn.close()


def start():
    server.listen()
    print(f"[LISTETNING] Server is listening on {SERVER}")
    started = True
    while started:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_test, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()
server.close()
