import threading as t
import socket as s

# See if the ip is valid.
def validate_ip_address(ip_address):
    try:
        s.inet_aton(ip_address)
        return True
    except s.error:
        return False

# See if the socket is valid.
def validate_socket(socket):
    try:
        socket = int(socket)
        if 1 <= socket <= 65535:
            return True
        else:
            return False
    except ValueError:
        return False

def get_connection():
    while True:
        ip_address = input("Enter an IP address: ")
        socket_number = input("Enter a socket number: ")

        if validate_ip_address(ip_address) and validate_socket(socket_number):
            break
        else:
            print("Invalid IP address or socket number. Please try again.")
    
    return ip_address, int(socket_number)

# Recieve messages from the server.
def recieve(client, nickname):
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            if (message == "4E 49 43 4B 4E 41 4D 45"):
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break

# Ask the user for the next message to send.
def send(client, nickname):
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode("ascii"))

def run_client():
    # Get user input
    IP, SOCKET = get_connection()
    nickname = input("What would you like your nickname to be? ")
    
    # Create client
    client = s.socket(s.AF_INET, s.SOCK_STREAM)
    client.connect((IP, SOCKET))

    # Start threads for sending and recieving messages
    recieve_thred = t.Thread(target=recieve, args=(client, nickname))
    send_thread = t.Thread(target=send, args=(client, nickname))

    recieve_thred.start()
    send_thread.start()

run_client()