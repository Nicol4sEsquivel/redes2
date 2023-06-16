import socket

# Configurar el host y el puerto del servidor
host = 'localhost'
port = 8080

# Crear un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
client_socket.connect((host, port))

while True:
    # Leer la entrada del usuario
    message = input("Ingrese un mensaje: ")

    # Enviar el mensaje al servidor
    client_socket.sendall(message.encode())

    # Esperar la respuesta del servidor
    response = client_socket.recv(1024).decode()

    # Imprimir la respuesta del servidor
    print("Respuesta del servidor:", response)

    # Terminar la conexión si se ingresa 'exit'
    if message == 'exit':
        break

# Cerrar el socket del cliente
client_socket.close()