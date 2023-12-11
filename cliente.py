import socket

def main():
    # Creamos el socket
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectamos al servidor en el puerto 8080
    clientsocket.connect(("localhost", 8080))

    # Iniciamos el juego
    intentos = 0
    contraseña = ""
    while intentos < 15:
        # Solicitamos un intento al usuario
        intento = input("Intento (1-9): ")

        # Enviamos el intento al servidor
        clientsocket.sendall(intento.encode("utf-8"))

        # Recibimos la respuesta del servidor
        respuesta = clientsocket.recv(1024).decode("utf-8")

        # Si la respuesta es "Intento correcto", actualizamos la contraseña
        if respuesta == "Intento correcto":
            print("Has adivinado un número correcto!")
            contraseña += intento

        # Si la contraseña está completa, mostramos el mensaje de ganador y cerramos la conexión
        if len(contraseña) == 5:
            print("Has ganado!")
            clientsocket.close()
            break

        # Si la contraseña no está completa, la mostramos parcialmente
        print("Contraseña actualizada:", contraseña[:len(contraseña)])

        # Incrementamos el contador de intentos
        intentos += 1

    # Cerramos la conexión
    clientsocket.close()

if __name__ == "__main__":
    main()
