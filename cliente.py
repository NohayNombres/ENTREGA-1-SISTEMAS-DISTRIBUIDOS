import socket
import sys

host = '129.151.109.134' # dirección IP del Servidor
puerto = 8080 # Puerto de conexión

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # se crea el objeto Socket de tipo internet(AD_INET) y protocolo tcp/ip(SOCK_STREAM)
cliente.connect((host, puerto))  # establecer la conexion y pasamos los datos de conexión
while True:
    mensaje= input("Seleccione una opcion:\n (1) Consignar a Cuenta\n (2) Consultar Cuenta \n (3) Salir \n") # Menu de opciones para el cliente
    cliente.send(mensaje.encode('utf-8')) # Envía opción del cliente al servidor
    dato = cliente.recv(1024) #Acepta los datos del socket y devuelve una cadena con un tamaño maximo de bufsize de 1024
    print(dato.decode('utf-8')) # Imprime mensaje recibido del servidor

    if mensaje == "1":
        cuenta = input("Ingrese numero de cuenta: ") # Se pide al cliente ingresar el número de cuenta
        monto = input("Ingrese valor a consignar: ") # Se pide al cliente ingresar el monto a consignar
        print("\n")
        total= (cuenta + "," + monto) # Se concatena cuenta y monto en una sola variable
        cliente.send(total.encode('utf-8')) # Envía numero de cuenta y saldo al servidor
        respuesta = cliente.recv(1024) #Acepta los datos del socket y devuelve una cadena con un tamaño maximo de bufsize de 1024
        print("Respuesta Servidor: " + respuesta.decode('utf-8'))

    elif mensaje == "2":
        numcuenta = input("Ingrese numero de cuenta a consultar: ") # Se pide al cliente ingrese el número de cuenta a consultar
        cliente.send(numcuenta.encode('utf-8')) # Se envia el numero de cuenta al servidor
        cuenta = cliente.recv(1024) #Acepta los datos del socket y devuelve una cadena con un tamaño maximo de bufsize de 1024
        print("Su saldo es: " + cuenta.decode('utf-8')+"\n") # Se imprime el saldo recibido del servidor

    elif mensaje == "3":
        print("Conexión cerrada")
        cliente.close() # Cierra la conexión
        break

    else:
        print("Opción no válida!!!") # SI el usuario ingresa un opción que no esta dentro del menú termina el programa
        cliente.close() # Cierra la conexión
        sys.exit() # cierra el programa