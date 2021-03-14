import ftp
import sqlite
import sqlite3
ejecucion = True
while ejecucion ==  True:
    class Programa():
        ejecucion = True
        sqlite.crear_db()
        seleccion = input('¿Que quieres hacer hoy?\n 1. Añadir servidor \n 2. Conectarte a un servidor \n 3. Conectarte  aun grupo de servidores \n 4. Salir ')
        if seleccion == '1':
            servidor = ftp.Servidor()
            servidor.guardar_servidor()
        if seleccion == '2':
            ftp.seleccionar_servidor()
        if seleccion == '4':
            print('Cerrando programa')
            ejecucion = False
    ejecucion = False




