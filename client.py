import socket
import threading
import json
import tkinter as tk
from vector_clock import VectorClock

class ChatClient:
    def __init__(self, root, host='127.0.0.1', port=12345):
        self.root = root
        self.root.title("Causal Ordered Chat")

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.vector_clock = VectorClock(self.client.getsockname()[1])

        self.chat_display = tk.Text(root, height=20, width=50)
        self.chat_display.pack()

        self.entry = tk.Entry(root, width=40)
        self.entry.pack()
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack()

        threading.Thread(target=self.receive_messages, daemon=True).start()

    def send_message(self):
        message = self.entry.get()
        if message:
            self.vector_clock.increment()
            data = {"message": message, "vector_clock": self.vector_clock.get_clock()}
            self.client.send(json.dumps(data).encode())
            self.entry.delete(0, tk.END)

    def receive_messages(self):
        while True:
            try:
                data = self.client.recv(1024).decode()
                if not data:
                    break
                message_data = json.loads(data)
                received_clock = message_data["vector_clock"]
                self.vector_clock.update(received_clock)

                self.chat_display.insert(tk.END, f"{message_data['message']} \n")
            except:
                break

if __name__ == "__main__":
    root = tk.Tk()
    client = ChatClient(root)
    root.mainloop()
