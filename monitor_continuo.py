import subprocess
import platform
import time  # <--- Nueva herramienta para controlar el tiempo

def monitorear_continuo(ip_maquina, intervalo_segundos):
    print(f"--- Iniciando Agente de Monitoreo ---")
    print(f"Monitoreando: {ip_maquina} cada {intervalo_segundos} segundos.")
    print("Presiona Ctrl+C para detener el script.")
    print("-" * 50)

    try:
        # Iniciamos el bucle infinito
        while True:
            parametro = "-n" if platform.system().lower() == "windows" else "-c"
            comando = ["ping", parametro, "3", ip_maquina]
            
            # Ejecutamos el ping
            resultado = subprocess.run(comando, stdout=subprocess.PIPE, text=True)
            texto_de_respuesta = resultado.stdout

            # Analizamos la respuesta
            if "TTL=" in texto_de_respuesta:
                print(f"[OK] {time.strftime('%H:%M:%S')} - {ip_maquina} está viva.")
            else:
                print(f"[ALERTA] {time.strftime('%H:%M:%S')} - {ip_maquina} NO RESPONDE.")

            # Pausamos el script para no saturar la red
            time.sleep(intervalo_segundos)
            
    except KeyboardInterrupt:
        # Esto permite cerrar el programa limpiamente con Ctrl+C
        print("\n--- Monitoreo detenido por el usuario ---")

# --- CONFIGURACIÓN ---
IP_A_REVISAR = "192.168.150.97" # Pon tu IP de Proxmox o VMware
SEGUNDOS_DE_ESPERA = 5        # Revisa cada 5 segundos

monitorear_continuo(IP_A_REVISAR, SEGUNDOS_DE_ESPERA)