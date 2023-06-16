import socket
import threading

# Configurar el host y el puerto del servidor
host = 'localhost'
port = 8080

# Crear un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket al host y puerto
server_socket.bind((host, port))

# Escuchar conexiones entrantes
server_socket.listen(5)
print("El servidor está escuchando en el puerto", port)

# Función para manejar las conexiones entrantes de clientes
def handle_client(client_socket, client_address):
    print("Conexión establecida con", client_address)

    while True:
        # Recibir datos del cliente
        data = client_socket.recv(1024).decode()

        if not data:
            break

        print("Mensaje recibido de", client_address, ":", data)

        # Responder al cliente
        response = "Mensaje recibido correctamente"
        client_socket.sendall(response.encode())

        # Terminar la conexión si se recibe 'exit'
        if data == 'exit':
            break

    # Cerrar el socket del cliente
    client_socket.close()
    print("Conexión cerrada con", client_address)

while True:
    # Aceptar conexiones entrantes
    client_socket, client_address = server_socket.accept()

    # Crear un hilo para manejar la conexión entrante
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
