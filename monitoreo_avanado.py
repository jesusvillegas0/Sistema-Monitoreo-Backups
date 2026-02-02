import subprocess
import platform
import time
from datetime import datetime

def registrar_log(mensaje):
    """Función para guardar mensajes en un archivo de texto"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"[{timestamp}] {mensaje}\n"
    
    # Abrimos el archivo en modo 'a' (append/añadir) para no borrar lo anterior
    with open("log_monitoreo.txt", "a", encoding="utf-8") as archivo:
        archivo.write(linea)

def chequear_ping(ip):
    """Hace un solo ping y devuelve True si tiene éxito, False si falla"""
    parametro = "-n" if platform.system().lower() == "windows" else "-c"
    comando = ["ping", parametro, "1", ip]
    
    resultado = subprocess.run(comando, stdout=subprocess.PIPE, text=True)
    return "TTL=" in resultado.stdout

def monitoreo_avanzado(ip, intervalo):
    print(f"--- Iniciando Sistema de Logs ---")
    print(f"Revisando intermitencia en {ip}... (Ctrl+C para salir)")

    try:
        while True:
            fallos = 0
            intentos_totales = 3

            # Hacemos 3 intentos seguidos
            for i in range(intentos_totales):
                if chequear_ping(ip):
                    print(f"  Intento {i+1}: OK")
                else:
                    print(f"  Intento {i+1}: FALLÓ")
                    fallos += 1
                time.sleep(1) # Espera un segundo entre micro-intentos

            # Analizamos los resultados de los 3 intentos
            if fallos == 0:
                estado = "ESTABLE"
                msg = f"Servidor {ip} está estable (0/{intentos_totales} fallos)."
            elif fallos >= 2:
                estado = "INTERMITENTE/CAÍDO"
                msg = f"ALERTA: Intermitencia detectada en {ip}. Fallaron {fallos}/{intentos_totales} intentos."
            else:
                estado = "INESTABLE (Leve)"
                msg = f"Aviso: Se perdió 1 paquete de {intentos_totales} en {ip}."

            # Imprimimos en pantalla y guardamos en el archivo
            print(f" >> RESULTADO: {estado}")
            registrar_log(msg)
            
            print(f"Esperando {intervalo} segundos para el siguiente ciclo...\n")
            time.sleep(intervalo)

    except KeyboardInterrupt:
        print("\nDeteniendo monitoreo...")

# CONFIGURACIÓN
IP_PROXMOX = "192.168.150.97" # Cambia por tu IP real
monitoreo_avanzado(IP_PROXMOX, 10)