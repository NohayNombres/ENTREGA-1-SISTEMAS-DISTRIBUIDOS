# coding=utf-8
import socket
import fnmatch

host='192.168.56.102'
puerto = 8080
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mi_socket.bind((host, puerto))

while True:
	mi_socket.listen(0)
	print(f"Servidor Activo [{host}:{puerto}] Aceptando conexiones!.")
	conexion, direccion = mi_socket.accept()
	try:
		print(f"Conexión establecida desde: {direccion}")
		while True:
			mensaje = conexion.recv(1024)
			opcion = mensaje.decode('utf-8')
			if opcion == "1":
				conexion.send("Accion -->> [CONSIGNACION A CUENTA]\n".encode('utf-8'))
				archivo = open("datos.txt","a")
				print("-->>[CONSIGNACION A CUENTA]")
				cuenta = conexion.recv(1024)
				account = cuenta.decode('utf-8')
				print("- Cuenta y Monto: "+ account)
				archivo.write(account + '\n')
				conexion.send(" OK \n".encode('utf-8'))
				archivo.close()

			elif opcion == "2":
				conexion.send("Accion -->> [CONSULTAR SALDO DE CUENTA]\n".encode('utf-8'))
				print("-->>[CONSULTA DE SALDO]")
				buscar = conexion.recv(1024)
				ctabuscar = buscar.decode('utf-8')
				ctabuscar1 = ("*"+ctabuscar+"*")
				print(" - Cuenta a Buscar: "+ctabuscar)
				with open("datos.txt", "r") as datos:
					cuentas = datos.read().split('\n')
				master = fnmatch.filter(cuentas, ctabuscar1)
				strmaster = str(master).strip("['']")
				posicion = cuentas.index(strmaster)
				saldo = cuentas[posicion]
				conexion.send(saldo.encode('utf-8'))

			elif opcion == "3":
				conexion.send("---SALIR---\n".encode('utf-8'))
				print(" Cliente desconectado ")
				break
	except :
		conexion.close()
