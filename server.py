import socket
import threading
import json

class ChatServer:
    def __init__(self, host='127.0.0.1', port=12345):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(5)
        print(f"Server started on {host}:{port}")

        self.clients = {}  # {client_socket: (address, vector_clock)}
        self.lock = threading.Lock()  

    def broadcast(self, message, sender_socket, sender_clock):
        with self.lock:
            for client, (addr, vector_clock) in self.clients.items():
                if client != sender_socket:
                    try:
                        client.send(json.dumps({"message": message, "vector_clock": sender_clock}).encode())
                    except:
                        client.close()
                        del self.clients[client]

    def handle_client(self, client_socket, address):
        with self.lock:
            self.clients[client_socket] = (address, {})

        while True:
            try:
                data = client_socket.recv(1024).decode()
                if not data:
                    break
                message_data = json.loads(data)
                sender_clock = message_data["vector_clock"]
                message = f"{address}: {message_data['message']}"

                print(f"Received: {message} with Clock: {sender_clock}")
                self.broadcast(message, client_socket, sender_clock)
            except:
                break

        with self.lock:
            del self.clients[client_socket]
        client_socket.close()

    def start(self):
        while True:
            client_socket, addr = self.server.accept()
            print(f"New connection from {addr}")
            threading.Thread(target=self.handle_client, args=(client_socket, addr)).start()

if __name__ == "__main__":
    ChatServer().start()
