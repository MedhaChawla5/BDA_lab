import socket
import sys

def main():
    host = '127.0.0.1'
    port = 12345
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((host, port))
        
        while True:
            message = input("Enter message to send to server (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break
            client_socket.send(message.encode())
    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
