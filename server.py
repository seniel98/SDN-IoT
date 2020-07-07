import socket


def set_up_connection(server_ip, port_number, sim_connections):
    server = set_up_server(server_ip, port_number)

    server.listen(int(sim_connections))  # Listen to x simultaneous connections
    print("Server listening on port:" + str(port_number))

    cli, addr = server.accept()  # Create a client socket connection and accept it
    print("Connected to: " + addr[0] + ":" + str(addr[1]))  # Print the connection is established

    return cli, server


def set_up_server(server_ip, port_number):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Initialize an object to work with the socket
    print("Socket created")

    try:
        server.bind((server_ip, int(port_number)))  # Server IP and port to listen
    except socket.error as msg:
        print(msg)

    print("Socket bind completed")

    return server


def transfer_data(cli, server):
    """Function that is responsible of dealing with the data from the IoT device.
    Processes and prints on console the humidity and temperature"""
    while True:
        data = cli.recv(1024)
        data = data.decode('utf-8')
        data_message = data.split(":")
        temperature = data_message[0]
        humidity = data_message[1]
        print("Temp: " + temperature + " ºC" + " Humidity: " + humidity + " %")

    # Unreachable code with this algorithm.
    cli.close()  # Close the client connection
    server.close()  # Close the server connection


def main():
    """Main function that executes the whole file. Creates a console to interact with the user
    in order to create a dynamic program"""

    print("################################")
    print("################################")
    print("SERVER OF IOT HUMIDITY AND TEMPERATURE SENSOR")
    print("################################")
    print("################################")
    print("")

    server_ip = input("Enter server IP: ")  # Set server IP
    while not server_ip:  # Requests for data until user inputs something
        server_ip = input("Enter server IP: ")
    print(server_ip.upper().strip() + " set!")

    print("________________________________")

    port = input("Enter port number: ")  # Set port number
    while not port:  # Requests for data until user inputs something
        port = input("Enter port number: ")
    print("Port " + port.upper().strip() + " set!")

    print("________________________________")

    sim_connections = input("Enter number of simultaneous connections: ")  # Set number of sim. conn.
    while not sim_connections:  # Requests for data until user inputs something
        sim_connections = input("Enter number of simultaneous connections: ")
    print(sim_connections.upper().strip() + " set!")

    print("________________________________")

    cli, server = set_up_connection(server_ip, port, sim_connections)
    transfer_data(cli, server)  # Call the function to set the connection


main()
