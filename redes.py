from datetime import datetime, timedelta
import requests
from notificaciones import Alerta

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