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

    # Recibimos el nivel de dificultad del cliente
    nivel = connection.recv(1024).decode("utf-8")

    # Si el nivel es válido, generamos la contraseña correspondiente
    if nivel == "1":
        intentos = 0
        contraseña = ""
        for i in range(5):
            contraseña += str(random.randint(1, 9))
        intentos_permitidos = 30
        connection.sendall(b"Nivel Facil")
    elif nivel == "2":
        intentos = 0
        contraseña = ""
        for i in range(5):
            contraseña += str(random.randint(1, 9))
        intentos_permitidos = 15
        connection.sendall(b"Nivel Normal")
    elif nivel == "3":
        intentos = 0
        contraseña = ""
        for i in range(5):
            contraseña += str(random.randint(1, 9))
        intentos_permitidos = 6
        connection.sendall(b"Nivel Dificil")
    else:
        # Si el nivel es inválido, cerramos la conexión
        connection.sendall(b"Nivel invalido")
        connection.close()
        return

    # Iniciamos el juego
    while intentos < intentos_permitidos or intentos == 0:
        # Recibimos el intento del cliente
        intento = connection.recv(1024).decode("utf-8")

        # Si el intento es correcto, actualizamos la contraseña
        if intento in contraseña:
            # No eliminamos el carácter coincidente de la contraseña
            pass
        else:
            # Si el intento es incorrecto, notificamos al cliente y aumentamos el contador de intentos
            connection.sendall(b"Intento incorrecto")
            intentos += 1

    # Si el cliente se quedó sin intentos, notificamos al cliente y terminamos el juego
    if intentos == intentos_permitidos:
        connection.sendall(b"Has perdido")
        connection.close()
        return

    # Envía una respuesta al cliente, incluso si el cliente no ha adivinado la contraseña
    connection.sendall(b"Has ganado")

    # Cerramos la conexión
    connection.close()

if __name__ == "__main__":
    main()
