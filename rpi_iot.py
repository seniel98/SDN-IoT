import time
import RPi.GPIO as GPIO
import Adafruit_DHT
import socket

DHTSensor = Adafruit_DHT.DHT11
GPIO_PIN = 17


def read_sensor_data():
    humidity, temperature = Adafruit_DHT.read_retry(DHTSensor, GPIO_PIN)

    if humidity is not None and temperature is not None:  # Check if the values are not empty
        print('Reading sensor data...')
        return humidity, temperature
    else:
        print('No sensor data available')
        return "no data", "no data"


def set_up_connection(server_ip, port_number):
    # Create a socket object
    client_socket = socket.socket()

    # Establishing the connection with the server
    client_socket.connect((server_ip, int(port_number)))

    return client_socket


def send_msg(client_socket):
    while True:
        humidity, temperature = read_sensor_data()

        # Check the data retrieved by the sensor
        print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))

        humid = str(humidity)
        temp = str(temperature)

        message = temp + ":" + humid

        client_socket.send(str.encode(message))

        time.sleep(2)  # Sends the data every 2 seconds


def main():

    print("################################")
    print("################################")
    print("IOT HUMIDITY AND TEMPERATURE SENSOR DEVICE")
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

    send_msg(set_up_connection(server_ip, port))

    # print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))


main()
