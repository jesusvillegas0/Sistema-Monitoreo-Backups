import json
from base_datos import BaseDatos

with open("servidores_backups.json", "r", encoding="utf-8") as archivo_config:
    servidores_db = json.load(archivo_config)

db = BaseDatos("backups_sistema.db")

for nombre, info in servidores_db.items():
    ruta = info["ruta"]
    prefijo = info["prefijo"]
    formato = info["formato_fecha"]

    db.insertar_servidor(nombre, ruta, prefijo, formato)

db.consultar_servidores()
#db.eliminar_datos()
db.conexion.close()


