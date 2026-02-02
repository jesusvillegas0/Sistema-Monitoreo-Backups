import os
import platform
import subprocess
from datetime import datetime
import json
import psutil
from plyer import notification
import winsound 

#infraestructura = {
#    "Proxmox": "192.168.150.97",
#    "Windows": "192.168.150.64",
#    "VMware": "192.168.150.98"
#}

with open("config.json", "r") as archivo_config:
            infraestructura = json.load(archivo_config)

class GestorArchivos:
    def __init__(self, nombre_carpeta):
        self.carpeta = nombre_carpeta

    def crear_directorio(self):
        if not os.path.exists(self.carpeta):
            os.makedirs(self.carpeta)
            print(f"Carpeta '{self.carpeta}' creada con exito.")
        else:
            print(f"La carpeta '{self.carpeta}' ya existe.")
    
    def escribir_log(self, mensaje):
        ruta_archivo = os.path.join(self.carpeta, "reporte.txt")
        with open(ruta_archivo, "a") as archivo:
            archivo.write(mensaje + "\n")

    def realizar_ping(self, nombre, ip):
        
        try:
            parametro = "-n" if platform.system().lower() == "windows" else "-c"
            comando = ["ping", parametro, "4", ip]
            
            print(f"Verificando {nombre} ({ip})...")
                
            resultado = subprocess.run(comando, stdout=subprocess.PIPE, text=True)
        
            if "TTL=" in resultado.stdout:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error tecnico al intentar ping a {nombre}: {e}")
            return False
    def obtener_estado_sistema(self):
        ram = psutil.virtual_memory()
        gigabytes = ram.available / (1024**3)
        return f"RAM disponible: {gigabytes:.2f} GB"
    
    def lanzar_alerta(self, servidor):
        #. Sonido: Frecuencia 1000Hz, Duracion 500ms
        winsound.Beep(500, 100)

        # Notificacion Visual
        notification.notify(
            "ALERTA DE INFRAESTRUCTURA",
            f"El servidor {servidor} no responde. Revisa los logs.",
            app_name="Monitor de Red",
            timeout=5)
    def verificar_backups(self, nombre_servidor):
        fecha_hoy = datetime.now().strftime("%Y_%m_%d")
        nombre_archivo = f"backup_{nombre_servidor}_{fecha_hoy}.txt"
        ruta = os.path.join(self.carpeta, nombre_archivo)

        if os.path.exists(ruta):
            peso = os.path.getsize(ruta) / (1024**2)
            print(f"Backup de {nombre_servidor} encontrado. Tamaño: {peso:.2f} MB")
            return True
        else:
            print(f"ALERTA: No se encontro el backup de {nombre_servidor}")
            return False

mi_gestor = GestorArchivos("Backups_Proxmox")
mi_gestor.crear_directorio()
estado = mi_gestor.obtener_estado_sistema()
print(estado)
mi_gestor.escribir_log(estado)

#mi_gestor.escribir_log("Iniciando backup del servidor Proxmox")
print("--- INICIANDO ESCANEO DE RED ---")

contador = 0
exitos = 0


for nombre, ip in infraestructura.items():
    esta_vivo = mi_gestor.realizar_ping(nombre, ip)

    if esta_vivo:
        print(f"{nombre} esta ONLINE")
        mi_gestor.verificar_backups(nombre)
        exitos += 1
    else:
        print(f"{nombre} esta OFFLINE")
        hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mensaje = f"[{hora_actual}] ERROR: El servidor {nombre} no responde"
        mi_gestor.escribir_log(mensaje)
        mi_gestor.lanzar_alerta(nombre)
        contador += 1
if contador > 0:
    print(f"Se encontraron {contador} servidores caidos!!")        

print("--- ESCANEO FINALIADO ---")
print(f"Escaneo completado: {exitos} ONLINE, {contador} OFFLINE")

