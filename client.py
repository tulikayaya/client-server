import socket #import socket module for communication

def send_request(client_socket, request): 

    # send the request (encoded as bytes) to the server through the client socket
    client_socket.send(request.encode())

    # receiving response from server and decoding it from bytes to string
    response = client_socket.recv(1024).decode()
    print("Result:", response)

def start_client():

    #creating new socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connecting the client socket to the server running on localhost at port 12345
    client_socket.connect(('localhost', 12345))
   
   #infinite loop to display choices and accept user input
    while True:
        print("\nOptions:")
        print("1. Perform calculation (e.g., '5 6 add')")
        print("2. Change value (e.g., 'change x to 8')")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            data = input("Enter x, y, and operation (e.g., '5 6 add'): ")
            send_request(client_socket, data)
        elif choice == "2":
            data = input("Enter change request (e.g., 'change x to 8'): ")
            send_request(client_socket, data)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

    #close the client socket when user chooses to exit
    client_socket.close()
    print("Client disconnected.")

if __name__ == "__main__":
    start_client()