import threading as t
import socket as s

# Define the host and port
HOST = '127.0.0.1'
PORT = 55555

# Create and bind the server
server = s.socket(s.AF_INET, s.SOCK_STREAM)
server.bind((HOST, PORT))

# Tell the server to start listening
server.listen()

clients = []
nicknames = []

# Send messages from server to all clients.
def broadcast(message):
    for client in clients:
        client.send(message)

# Handles a client connection to the server.
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            nickname = nicknames[index]
            broadcast(f"{nickname} has left the chat.".encode('ascii'))
            nicknames.remove(nickname)
            break
    
    return

# 
def recieve():
    print("Server Running.")
    while True:
        # Accept a client connection
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # Ask the client for the nickname
        client.send("4E 49 43 4B 4E 41 4D 45".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")
        clients.append(client)
        nicknames.append(nickname)
        print(f"Client {client} bound to nickname {nickname}.")

        # Notify the clients that the user has joined the chat.
        client.send("Connected to server!".encode('ascii'))
        broadcast(f"{nickname} joined the chat.".encode("ascii"))

        # Open a thread to handle the client
        thread = t.Thread(target=handle, args=(client, ))
        thread.start()

# Boot the server
print("Server Starting...")
recieve()