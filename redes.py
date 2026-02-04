from datetime import datetime
import requests
from notificaciones import Alerta
import platform, subprocess

fecha_hora_act = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")


class MonitorWeb:
    def chequear_web(self, url, gestor):
        print(f"---- Chequeando pagina: {url}")
        try:
            respuesta = requests.get(url, timeout=15)
            if respuesta.status_code == 200:
                msg = f"La pagina {url} esta SALUDABLE"
                print(f"{msg} - {fecha_hora_act}")
                gestor.escribir_log(f"{msg} - {fecha_hora_act}")
            else:
                msg = f"ALERTA: {url} respondio con codigo {respuesta.status_code}"
                print(msg)
                mi_alerta = Alerta()
                mi_alerta.lanzar_alerta(f"web {url}")
        except requests.exceptions.RequestException as e:
            print(f"Error de conexion o tiempo: {e}")
    def realizar_ping(self,ip, gestor):
        
        try:
            print(f"\n--- Iniciando chequeo: {ip} ---")

            parametro = "-n" if platform.system().lower() == "windows" else "-c"
            
            comando = f"ping {parametro} 4 {ip}"
            
            resultado = subprocess.run(comando, stdout=subprocess.PIPE, text=True)

            texto_de_respuesta = resultado.stdout

            # Buscamos palabras clave que indican exito real
            if "TTL=" in texto_de_respuesta:
                print(f"\nEXITO: La VM {ip} respondio correctamente.")
                msg = f"El servidor con la IP: {ip} esta activo."
                gestor.escribir_log(f"{msg}, {fecha_hora_act}")
            elif "inaccesible" in texto_de_respuesta.lower():
                print(f"ERROR: El host {ip} es inaccesible (Ruta no encontrada).")
                msg = f"El servidor con la IP: {ip} no esta activo."
                gestor.escribir_log(f"{msg}, {fecha_hora_act}")
            else:
                print(f"ALERTA: No se pudo contactar con {ip}. Posiblemente apagada.")
        except Exception as e:
            print(f"Error al intentar ping a {ip}: {e}")
            return False