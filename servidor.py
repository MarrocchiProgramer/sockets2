import socket
import random

def main():
    # Creamos el socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bindeamos el socket al puerto 8080
    serversocket.bind(("localhost", 8080))

    # Escuchamos conexiones entrantes
    serversocket.listen(5)

    # Aceptamos una conexión entrante
    connection, address = serversocket.accept()

    # Generamos una contraseña aleatoria
    contraseña = ""
    for i in range(5):
        contraseña += str(random.randint(1, 9))

    # Iniciamos el juego
    intentos = 0
    while intentos < 15:
        # Recibimos el intento del cliente
        intento = connection.recv(1024).decode("utf-8")

        # Si el intento es correcto, actualizamos la contraseña
        if intento not in contraseña:
            contraseña = contraseña.replace(intento, "")
            connection.sendall(b"Intento correcto")
        else:
            # Si el intento es incorrecto, notificamos al cliente y aumentamos el contador de intentos
            connection.sendall(b"Intento incorrecto")
            intentos += 1

    # Si el cliente se quedó sin intentos, notificamos al cliente y terminamos el juego
    if intentos == 15:
        connection.sendall(b"Has perdido")

    # Cerramos la conexión
    connection.close()

if __name__ == "__main__":
    main()
