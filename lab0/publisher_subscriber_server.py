from collections import defaultdict

import socket
import threading

class PubSubServer:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type, client_socket):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(client_socket)

    def unsubscribe(self, event_type, client_socket):
        if event_type in self.subscribers and client_socket in self.subscribers[event_type]:
            self.subscribers[event_type].remove(client_socket)

    def publish(self, event_type, message):
        if event_type in self.subscribers:
            subscribers = self.subscribers[event_type][:]
            for client_socket in subscribers:
                try:
                    client_socket.send(message.encode())
                except socket.error:
                    print(f"Error sending message to {client_socket.getpeername()}")
                    self.unsubscribe(event_type, client_socket)

def handle_client(client_socket, pubsub_server):
    while True:
        try:
            message = client_socket.recv(1024).decode().strip()
            if not message:
                break
            print(f"Received message from client {client_socket.getpeername()}: {message}")
            pubsub_server.publish("event1", message)
        except socket.error as e:
            print(f"Socket error: {e}")
            break
    client_socket.close()
    print(f"Connection closed for client {client_socket.getpeername()}")

def main():
    host = '127.0.0.1'
    port = 12345
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)
    
    pubsub_server = PubSubServer()

    print(f"Server started on {host}:{port}")

    try:
        while True:
            client_socket, client_addr = server_socket.accept()
            print(f"Accepted connection from {client_addr}")
            
            client_handler = threading.Thread(target=handle_client, args=(client_socket, pubsub_server))
            client_handler.start()
    except KeyboardInterrupt:
        print("Server interrupted. Closing...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()

