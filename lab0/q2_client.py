import socket

def main():
    # Configure the client
    host = '127.0.0.1'
    port = 12345

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))

    # Get filename from user input
    filename = input("Enter filename: ")

    # Send filename to server
    client_socket.send(filename.encode())

    # Receive word count from server
    word_count = client_socket.recv(1024).decode()

if __name__ == '__main__':
    main()
