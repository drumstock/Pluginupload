import sqlite3
def crear_db():
    #Conexion
    conexion = sqlite3.connect('ftp.db')
    #crear cursor
    cursor = conexion.cursor()


    #Crear tabla
    cursor.execute("CREATE TABLE IF NOT EXISTS servidores"
                   "("+
                   "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   "grupo varchar(255) UNIQUE, " +
                   "servidor varchar(255) UNIQUE, " +
                   "usuario varchar(255), " +
                   "password varchar(255)," +
                   "localdir varchar(255)," +
                   "remotedir varchar(255)" +
                   ")")













    conexion.close()


