# client-server
This program consists of a server and a client that communicate over a network using sockets. The client sends requests to the server to perform calculations or change values, and the server processes these requests and sends back the results.
# Prereqs
1. Python 3.x: Must have Python 3 installed on system.
2. Socket Module: The program uses Python's built-in socket module, so no additional installations are required.

# Start The Server
1. Open a terminal or command prompt.
2. Navigate to the directory where server.py is located.
3. Run the server script using the following command: python server.py
4. The server will print : "Server is listening on port 12345..."

# Start The Client
1. Open another terminal or command prompt.
2. Navigate to the directory where client.py is located.
3. Run the client script using the following command: python client.py
4. The client will connect to the server and display the menu of choices.

# Client Side
Once it's connected, the menu options can be seen as below:
Options:
1. Perform calculation (e.g., '5 6 add')
2. Change value (e.g., 'change x to 8')
3. Exit
Enter your choice:

# Performing Calculation
Enter a calculation request in the format x y operation, where x and y are integers, and operation is one of add, subtract, multiply, or divide.
Example: Enter x, y, and operation (e.g., '5 6 add'): 5 6 add
The server will calculate the result and send it back to the client

# Performing Change Operation
Enter a change request in the format change x to x_value or change y to y_value, where: x_value or y_value is the new integer value. Example: Enter change request (e.g., 'change x to 8'): change x to 8
The server will update the value of x or y and re-perform the last operation with the updated values.

# Exiting 
Enter 3 to exit the program.

# Key Notes:
1. Ensure the server is running before starting the client.
2. The server and client must be running on the same machine (localhost). If running on different machines, you might want to replace 'localhost' with the server's IP address in client.py.
3.The server can handle only one client at a time.

# Troubleshooting
1. Port Already in Use: Ensure no other program is using port 12345 or change the port number in both server.py and client.py.
2. Connection Errors: If the client cannot connect to the server, ensure the server is running and there are no firewall or network issues.
