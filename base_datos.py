import sqlite3

class BaseDatos:
    def __init__(self, nombre_bd):
        self.conexion = sqlite3.connect(nombre_bd)
        self.cursor = self.conexion.cursor()
        self.crear_tablas()
    
    def crear_tablas(self):
        orden_sql = """
        CREATE TABLE IF NOT EXISTS servidores(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT UNIQUE NOT NULL,
        ruta TEXT NOT NULL,
        prefijo TEXT NOT NULL,
        formato_fecha TEXT NOT NULL)
        """
        self.cursor.execute(orden_sql)
        self.conexion.commit()
    
    def insertar_servidor(self, nombre, ruta, prefijo, formato_fecha):
        orden_sql = "INSERT INTO servidores (nombre, ruta, prefijo, formato_fecha) VALUES (?, ?, ?, ?)"
        self.cursor.execute(orden_sql, (nombre, ruta, prefijo, formato_fecha))
        self.conexion.commit()
        print(f"Servidor '{nombre}' guardado en la BD.")

    def consultar_servidores(self):
        orden_sql = "SELECT * FROM servidores"
        self.cursor.execute(orden_sql)
        
        servidores = self.cursor.fetchall()

        for fila in servidores:
            print(f"ID: {fila[0]} | Nombre: {fila[1]} | Ruta: {fila[2]} | Formato: {fila[3]}")
        
        return servidores
    
    def eliminar_datos(self):
        orden_sql = "DELETE FROM servidores"
        self.cursor.execute(orden_sql)

        servidores = self.cursor.fetchall()

        print(servidores)