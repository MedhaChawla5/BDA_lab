import socket

def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return -1  # File not found error code

def main():
    # Configure the server
    host = '127.0.0.1'
    port = 12345

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((host, port))

    # Start listening for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}...")

    while True:
        # Accept incoming connection
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        # Receive filename from client
        filename = client_socket.recv(1024).decode()
        print(f"Received filename from client: {filename}")

        # Count words in the file
        word_count = count_words_in_file(filename)

        print(f"No. of words in the file : {word_count}")
        
if __name__ == '__main__':
    main()
