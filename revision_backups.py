import os
from datetime import datetime, timedelta
import json
from plyer import notification
import winsound 
import requests, time

ayer_obj = datetime.now() - timedelta(days=1)

print(f"--- INICIANDO REVISIÓN DE BACKUPS (Fecha: {ayer_obj.strftime('%d/%m/%Y')}) ---")

with open("servidores_backups.json", "r", encoding="utf-8") as archivo_config:
    servidores_db = json.load(archivo_config)

class GestorArchivos:
    def __init__(self, nombre_carpeta):
        self.carpeta = nombre_carpeta

    def crear_directorio(self):
        if not os.path.exists(self.carpeta):
            os.makedirs(self.carpeta)
            print(f"Carpeta '{self.carpeta}' creada con exito.")
        else:
            print(f"La carpeta '{self.carpeta}' ya existe.")

    def lanzar_alerta(self, backup):
        #. Sonido: Frecuencia 1000Hz, Duracion 500ms
        winsound.Beep(500, 100)

        # Notificacion Visual
        notification.notify(
                "ALERTA DE BACKUPS",
                f"No se encontro el {backup}. Revisa!!!",
                app_name="Monitor de Red",
                timeout=5)
    def escribir_log(self, mensaje):
        ruta_archivo = os.path.join(self.carpeta, "reporte.txt")
        with open(ruta_archivo, "a", encoding="utf-8") as file:
            file.write(mensaje + "\n")

    def chequear_web(self, url):
        print(f"---- Chequeando pagina: {url}")
        try:
            respuesta = requests.get(url, timeout=15)
            if respuesta.status_code == 200:
                msg = f"La pagina {url} esta SALUDABLE"
                print(msg)
                mi_gestor.escribir_log(msg)
            else:
                msg = f"ALERTA: {url} respondio con codigo {respuesta.status_code}"
                print(msg)
                mi_gestor.lanzar_alerta(f"Web {url}")
        except TimeoutError:
            print("Error en monitoreo web")

    def limpiar_archivos_viejos(self, ruta_carpeta, prefijos, dias=15):
        ahora = time.time()
        segundos_en_un_dia = 86400 # 24 * 60 * 60
        limite = ahora - (dias * segundos_en_un_dia)
        
        print(f"\n--- Iniciando limpieza en: {ruta_carpeta} ---")
        
        try:
            files = os.listdir(ruta_carpeta)
            for file in files:
                # Solo revisamos archivos que coincidan con nuestro prefijo
                if file.startswith(prefijos):
                    rutas_completas = os.path.join(ruta_carpeta, file)
                    
                    # Obtenemos la fecha de modificación
                    fecha_archivo = os.path.getmtime(rutas_completas)
                    
                    if fecha_archivo < limite:
                        # Cálculo para mostrar cuántos días han pasado (opcional)
                        dias_antiguedad = (ahora - fecha_archivo) / segundos_en_un_dia
                        print(f"🧹 [BORRADO SIMULADO]: {file} ({dias_antiguedad:.1f} días de antigüedad)")
                        
                        # CUANDO ESTÉS LISTO, DESCOMENTA LA LÍNEA DE ABAJO:
                        # os.remove(ruta_completa) 
                        
        except Exception as e:
            print(f"⚠️ Error al limpiar la carpeta: {e}")

mi_gestor = GestorArchivos("Backups_Proxmox")
# EL BUCLE MAESTRO
for nombre, info in servidores_db.items():
    # Extraemos los datos del diccionario interno
    ruta_remota = info["ruta"]
    prefijo = info["prefijo"]
    formato = info["formato_fecha"]

    fecha_formateada = ayer_obj.strftime(formato)
    busqueda_final = f"{prefijo}{fecha_formateada}"
    
    print(f"\nRevisando {nombre}...")

    try:
        # Listamos los archivos de esta ruta específica
        archivos = os.listdir(ruta_remota)
        encontrado = False

        for archivo in archivos:
            if archivo.startswith(busqueda_final):
                ruta_completa = os.path.join(ruta_remota, archivo)
                peso = os.path.getsize(ruta_completa) / (1024**2)
                
                print(f" ¡ÉXITO! Archivo: {archivo}")
                print(f" Tamaño: {peso:.2f} MB")
                mi_gestor.escribir_log(f"Fecha: {ayer_obj.strftime('%d/%m/%Y %H:%M:%S')} Server Revisado {nombre}, Backup: {archivo}, Tamaño: {peso:.2f} MB")
                encontrado = True
                mi_gestor.limpiar_archivos_viejos(ruta_remota, prefijo, dias=15)
                break # Si ya lo encontramos, no hace falta seguir viendo esa carpeta
        
        if not encontrado:
            print(f" ALERTA: No se encontró ningún backup con prefijo {busqueda_final}")
            mi_gestor.lanzar_alerta(busqueda_final)

    except (FileNotFoundError, PermissionError) as e:
        # Si falla un servidor (por red o permisos), el script sigue con el siguiente
        print(f" ERROR DE ACCESO O RUTA. {e}")
    except OSError as e:
        print(f" ERROR DE ACCESO O RUTA. {e}")
mi_gestor.chequear_web("https://procuracenter.com.ve/")
print("\n--- PROCESO FINALIZADO ---")