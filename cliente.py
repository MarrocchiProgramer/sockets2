import socket

def main():
    # Creamos el socket
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectamos al servidor
    clientsocket.connect(("localhost", 8080))

    # Mostramos un menú
    print("Facil: 1 ,Medio: 2, Dificil: 3")

    # Leemos la entrada del usuario
    nivel = input("Ingrese el nivel de dificultad: ")

    # Enviamos el nivel de dificultad al servidor
    clientsocket.sendall(nivel.encode("utf-8"))

    # Recibimos la contraseña del servidor
    contraseña = clientsocket.recv(1024).decode("utf-8")

    # Iniciamos el juego
    while True:
        # Solicitamos un intento al usuario
        intento = input("Intento (1-9): ")

        # Enviamos el intento al servidor
        clientsocket.sendall(intento.encode("utf-8"))

        # Recibimos la respuesta del servidor
        respuesta = clientsocket.recv(1024).decode("utf-8")

        # Imprimimos la respuesta del servidor
        print(respuesta)

        # Si el usuario ha ganado, terminamos el juego
        if respuesta == "Has ganado!":
            break

    # Cerramos la conexión
    clientsocket.close()

if __name__ == "__main__":
    main()
