# Python Socket-Based Calculator

## Overview
This repository contains a simple socket-based client-server calculator application. The server listens for incoming client connections and performs basic arithmetic operations (`add`, `subtract`, `multiply`, `divide`) based on client requests. Clients can also request to change operand values and receive updated results.

## Code Explanation

### 1. Server Implementation
The server runs a socket listener on `localhost:12345` and waits for client connections. It supports the following operations:
- Addition (`add`)
- Subtraction (`subtract`)
- Multiplication (`multiply`)
- Division (`divide`), with error handling for division by zero
- Changing operand values dynamically

#### Importing Required Modules
```python
import socket
```
- `socket` is used to establish a server-client connection.

#### Function to Handle Calculations
```python
def calculate(x, y, operation):
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y
    elif operation == "multiply":
        return x * y
    elif operation == "divide":
        if y == 0:
            return "Error: Division by zero"
        return x / y
    else:
        return "Error: Invalid operation"
```
- Takes two numbers and an operation as input.
- Returns the computed result or an error message.

#### Handling Change Requests
```python
if data.startswith("change"):
    parts = data.split()
    if parts[1] == "x":
        x = int(parts[3])
    elif parts[1] == "y":
        y = int(parts[3])
    else:
        response = "Error: Invalid change request"
        client_socket.send(response.encode())
        continue

    if last_operation:
        result = calculate(x, y, last_operation)
        response = str(result)
    else:
        response = "Error: No previous operation to perform"
```
- The client can send a change request to modify `x` or `y`.
- The server updates the respective variable and, if a previous operation exists, recalculates the result with the updated value.
- The new result is sent back to the client.

### 2. Client Implementation
The client connects to the server and sends requests for calculations or value updates.

#### Connecting to the Server
```python
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
```
- Establishes a connection to the server at `localhost:12345`.

#### Sending Requests to Server
```python
def send_request(client_socket, request):
    client_socket.send(request.encode())
    response = client_socket.recv(1024).decode()
    print("Result:", response)
```
- Sends encoded requests to the server.
- Receives and prints the server's response.

#### User Interaction
```python
while True:
    print("\nOptions:")
    print("1. Perform calculation (e.g., '5 6 add')")
    print("2. Change value (e.g., 'change x to 8')")
    print("3. Exit")
    choice = input("Enter your choice: ")
```
- Provides a menu for users to perform calculations, update values, or exit.

## Expected Output
### Example 1: Performing a Calculation
```
Options:
1. Perform calculation (e.g., '5 6 add')
2. Change value (e.g., 'change x to 8')
3. Exit
Enter your choice: 1
Enter x, y, and operation (e.g., '5 6 add'): 7 8 add
Result: 15
```

### Example 2: Changing a Value and Recalculating
```
Enter your choice: 2
Enter change request (e.g., 'change x to 8'): change x to 8
Result: 16
```

## Diagram
![Socket Communication](path/to/image.png)

## Installation and Usage
1. Clone this repository:
   ```sh
   git clone https://github.com/tulikayaya/client-server.git
   cd repository
   ```
2. Start the server:
   ```sh
   python server.py
   ```
3. Start the client:
   ```sh
   python client.py
   ```

