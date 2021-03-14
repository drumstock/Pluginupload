import os
import ftplib
import ftputil
import sqlite3
import sqlite
sqlite.crear_db()
def subida(ftp,local_dir = "C:/plugins/", ftp_dir = "/wp-content/plugins/"):
    with ftp as ftp_host:
        def upload_dir(localDir, ftpDir):
            list = os.listdir(localDir)
            for fname in list:
                if os.path.isdir(localDir + fname):
                    if(ftp_host.path.exists(ftpDir + fname) != True):
                        ftp_host.mkdir(ftpDir + fname)
                        print(ftpDir + fname + " ha sido creado.")
                    upload_dir(localDir + fname + "/", ftpDir + fname + "/")
                    mensaje = 'El plugin ha sido creado con éxito, no olvides activarlo desde el panel de administración de wordpress'
                else:
                    if(ftp_host.upload_if_newer(localDir + fname, ftpDir + fname)):
                        print(ftpDir + fname + " ha sido actualizado.")
                        mensaje = "La actualización se ha completado con éxito"
                    else:
                        print(localDir + fname + " ya existe esta versión del archivo.")
                        mensaje = "Esta versión del plugin ya existe"
                    print(mensaje)




        upload_dir(local_dir, ftp_dir)

class Servidor():

    def guardar_servidor(self):
        conexion = sqlite3.connect('ftp.db')
        print('La base de datos seleccionada es: ftp.db')
        servidor = input('Introduce el servidor al que conectarte ')
        usuario = input('Introduce el usuario ')
        password = input('Introduce la contraseña ')
        grupo = input("¿A que grupo de cliente pertenece este servidor FTP?")
        local_dir = input('Seleccione la ruta local donde se encuentran los plugins')
        remote_dir = input('Seleccione la carpeta remota donde se alojan los plugins')
        cursor = conexion.cursor()
        comprobacion = cursor.execute(("SELECT servidor FROM servidores"))
        dbmaquina = comprobacion.fetchall()

        try:
            cursor.execute("INSERT INTO servidores (grupo, servidor, usuario, password, localdir, remotedir)values(?, ?, ?, ?, ?, ?)",(grupo, servidor, usuario, password,local_dir,remote_dir))
            conexion.commit()
            print('Añadido a la base de datos correctamente')
        except:
            print('Este servidor FTP ya existe ')
            entrada = input('¿quieres actualizarlo?')
            if entrada == 'si':
                cursor.execute("UPDATE servidores SET grupo=?, usuario=?, password=?, localdir=?, remotedir=? WHERE servidor=?", (grupo, usuario, password, local_dir,remote_dir, servidor))
                conexion.commit()
                print('Servidor actualizado')
            else:
                entrada = input('¿Quieres borrar este servidor?')
                if entrada =='si':
                    cursor.execute('DELETE FROM servidores WHERE servidor=?', (servidor))
                    conexion.commit()
                    print('Servidor ' +servidor+ ' ha sido eliminado correctamente')

def seleccionar_servidor():
    conexion = sqlite3.connect('ftp.db')
    cursor = conexion.cursor()
    comprobacion = cursor.execute(("SELECT * FROM servidores"))
    servers = conexion.commit()
    servidores = comprobacion.fetchall()
    for x in servidores:
        print('---------------------')
        print('ID: ', x[0])
        print('Servidor: ', x[1])
        print('---------------------')
    seleccion = input('Introduce la ID del servidor al que quieres conectarte')

    eleccion = cursor.execute("SELECT * FROM servidores WHERE id=?", str(seleccion))
    sql_consulta = conexion.commit()
    listado = eleccion.fetchall()
    ftp = Servidor()
    for x in listado:
        servidor = x[2]
        usuario = x[3]
        password = x[4]
        conectado = ftputil.FTPHost(servidor, usuario, password)
        print('Conectado con exito')
        respuesta = input('¿Quieres Actualizar los plugins?')
        if respuesta == 'si':
            subida(conectado, x[5], x[6])









