import subprocess
import platform
import time
from datetime import datetime

# --- FUNCIONES DE APOYO ---

def registrar_log(mensaje):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log_monitoreo.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{timestamp}] {mensaje}\n")

def chequear_ping(ip):
    parametro = "-n" if platform.system().lower() == "windows" else "-c"
    comando = ["ping", parametro, "1", ip]
    resultado = subprocess.run(comando, stdout=subprocess.PIPE, text=True)
    return "TTL=" in resultado.stdout

# --- FUNCIÓN PRINCIPAL ---

def monitoreo_con_metricas(ip, intervalo):
    # 1. Inicializamos los contadores (Empiezan en cero)
    total_chequeos = 0
    total_caidas = 0
    
    print(f"--- Monitor Pro ---")
    print(f"(Ctrl+C para salir)")
    print(f"Objetivo: {ip} | Reporte: log_monitoreo.txt")
    print("-" * 50)

    try:
        while True:
            total_chequeos += 1  # Sumamos un chequeo cada vez que inicia el bucle
            fallos_en_esta_ronda = 0
            
            print(f"Chequeo #{total_chequeos} en curso...")

            # Ráfaga de 3 pings
            for i in range(3):
                if chequear_ping(ip):
                    print(f"  [{i+1}] OK")
                else:
                    print(f"  [{i+1}] FALLO")
                    fallos_en_esta_ronda += 1
                time.sleep(0.5)

            # 2. Lógica de decisión y actualización de contador global
            if fallos_en_esta_ronda >= 2:
                total_caidas += 1  # <--- ¡Aquí sumamos la caída al contador global!
                estado = "CAÍDO/INTERMITENTE"
                alerta = f"¡ALERTA! El servidor falló {fallos_en_esta_ronda}/3 pings."
            else:
                estado = "ESTABLE"
                alerta = "Conexión estable."

            # 3. Mostrar resumen en consola
            print(f"Estado actual: {estado}")
            print(f"ESTADÍSTICAS: Total caídas: {total_caidas} | Total intentos: {total_chequeos}")
            print("-" * 30)

            # Guardamos el resumen en el log
            registrar_log(f"Ciclo {total_chequeos}: {estado} - Caídas totales: {total_caidas}")

            time.sleep(intervalo)

    except KeyboardInterrupt:
        print(f"\nMonitoreo finalizado. Total de fallos registrados: {total_caidas}")

# CONFIGURACIÓN
IP_A_MEDIR = "192.168.150.97" 
monitoreo_con_metricas(IP_A_MEDIR, 10)