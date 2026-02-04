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
            print(f"ID: {fila[0]} | Nombre: {fila[1]} | Ruta: {fila[2]} | Prefijo: {fila[3]} | formato: {fila[4]}")
        
        return servidores
    
    def eliminar_datos(self):
        orden_sql = "DELETE FROM servidores"
        self.cursor.execute(orden_sql)

        servidores = self.cursor.fetchall()

        print(servidores)

    def agregar_servidor_interativo(self):
        print("\n--- Agregar Nuevo servidor al Monitoreo ---")
        nombre = input("Nombre del servidor: ")
        ruta = input("Ruta de red (ej. \\\\192.168...): ")
        prefijo = input("Prefijo del archivo: ")
        formato = input("Formato de fecha (ej. %Y-%m-%d): ")

        try:
            self.insertar_servidor(nombre, ruta, prefijo, formato)
            print("Servidor agregado con exito.")
        except Exception as e:
            print(f"Error al agregar: {e}")

    def eliminar_servidor(self, id_servidor):
        orden_sql = "DELETE FROM servidores WHERE id = ?"
        self.cursor.execute(orden_sql, (id_servidor,))
        self.conexion.commit()

        print(f"\nServidor con el {id_servidor} borrado con exito!!")

    def actualizar_servidor(self, id_servidor, nombre, ruta, prefijo, formato):
        orden_sql = "UPDATE servidores SET nombre = ?, ruta = ?, prefijo = ?, formato_fecha = ? WHERE id = ?"
        self.cursor.execute(orden_sql, (nombre, ruta, prefijo, formato, id_servidor))
        self.conexion.commit()

        print(f"El servidor {nombre} fue actualizado con exito...")