import socket

#function to handle calculation request sent from the client
def calculate(x, y, operation):
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y
    elif operation == "multiply":
        return x * y
    elif operation == "divide":
        if y == 0:

            #handle edge cases, such as division by zero
            return "Error: Division by zero"
        return x / y
    else:
        return "Error: Invalid operation"

def start_server():
    #creating a new socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #binding the socket to the localhost IP address and port 12345
    server_socket.bind(('localhost', 12345))

    #listening for incoming connections
    server_socket.listen(1)

    #printing so as to simulate that server is running
    print("Server is listening on port 12345...")


    x, y = 0, 0  

    #initialising last operation so that a change request can also return the changed result
    last_operation = None  
    
    #infinite loop
    while True:

        # accept an incoming connection from a client
        # client_socket is the socket object for the client, and addr is the client's address
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} established.")

        #loop to handle communication with the connected client
        while True:

            #should receive 1024 bytes of data to decode or else we just break the loop
            data = client_socket.recv(1024).decode()
            if not data:
                break

            if data.startswith("change"):
                #if it's a change request, split the data based on spaces
                parts = data.split()

                #update the new value of x if client wants to change x
                if parts[1] == "x":
                    x = int(parts[3])
                #update the new value of y if client wants to change y
                elif parts[1] == "y":
                    y = int(parts[3])
                else:
                    response = "Error: Invalid change request" #else send invalid response
                    client_socket.send(response.encode())
                    continue

                # performing the last operation again with the updated values to return the updated result
                if last_operation:
                    result = calculate(x, y, last_operation)
                    response = str(result)
                else:
                    response = "Error: No previous operation to perform"
            else:
                # handle calculation request
                try:
                    parts = data.split()
                    x = int(parts[0]) #extrcat x
                    y = int(parts[1]) #extract y
                    operation = parts[2] #extract 'add', 'multiply' etc
                    last_operation = operation  # store the last operation
                    result = calculate(x, y, operation) # calculate result
                    response = str(result) #send result as response
                except Exception as e:
                    response = f"Error: {str(e)}"

            client_socket.send(response.encode())

        client_socket.close()
        print(f"Connection with {addr} closed.")

if __name__ == "__main__":
    start_server()