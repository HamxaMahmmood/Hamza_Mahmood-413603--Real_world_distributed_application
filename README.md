# Causal Ordered Chat Application  

## **Introduction**  
This is a **multi-client chat application** that ensures **causal message ordering** using **Vector Clocks**. The system allows multiple clients to communicate through a central server while preserving the correct sequence of events in distributed communication.

## **Features**  
- **Multi-client communication** via a threaded server  
- **Causal ordering enforcement** using **Vector Clocks**  
- **Tkinter GUI** for user-friendly chat interaction  
- **SQLite database** for storing chat history  
- **Threading for concurrent message handling**  

---

## **System Architecture**  

The application follows a **client-server model**:  

### **Components**  
1. **Server (`server.py`)**  
   - Handles multiple clients and manages causal message ordering.  
2. **Client (`client.py`)**  
   - Tkinter GUI for sending and receiving messages.  
3. **Vector Clock (`vector_clock.py`)**  
   - Implements vector clock logic for causal ordering.  
4. **Database (`database.py`)**  
   - Stores chat messages persistently using SQLite.  

### **Message Flow**  
1. A client sends a message with its **vector clock**.  
2. The server **updates clocks and broadcasts** the message while maintaining causal order.  
3. Each client **updates its clock** and displays messages in the correct sequence.  

---

## **Installation and Setup**  

### **🔹 Prerequisites**  
Ensure you have **Python 3** installed.  

Install required libraries using:  
```bash
pip install sqlite3

 ```
### Running the Application
### **Start the Server**
Run the following command in a terminal:

```bash

python server.py
```
This initializes the server to accept client connections.

 ### **Start Multiple Clients**
Open multiple terminals and run:

```bash

python client.py
```
Each instance represents a separate chat user.

### **Send Messages**
Type a message in the input box.
Messages will appear in causal order across all clients.
