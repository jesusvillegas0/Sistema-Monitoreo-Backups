#import os
import platform
import subprocess

def monitorear_con_detalle(ip_maquina):
    print(f"--- Iniciando chequeo: {ip_maquina} ---")
    
    # Determinamos el parámetro según el sistema operativo (Windows usa -n, Linux -c)
    parametro = "-n" if platform.system().lower() == "windows" else "-c"
    
    # Construimos el comando de consola: ping -n 1 [IP]
    comando = f"ping {parametro} 4 {ip_maquina}"
    
    # Ejecutamos y capturamos la salida del texto
    # stdout=subprocess.PIPE nos permite guardar lo que el ping escribe
    resultado = subprocess.run(comando, stdout=subprocess.PIPE, text=True)

    texto_de_respuesta = resultado.stdout

    # Buscamos palabras clave que indican exito real
    if "TTL=" in texto_de_respuesta:
        print(f"EXITO: La VM {ip_maquina} respondio correctamente.")
    elif "inaccesible" in texto_de_respuesta.lower():
        print(f"ERROR: El host {ip_maquina} es inaccesible (Ruta no encontrada).")
    else:
        print(f"ALERTA: No se pudo contactar con {ip_maquina}. Posiblemente apagada.")
    
    
    # Ejecutamos el comando y guardamos la respuesta
    #respuesta = os.system(comando)

    # En programación, 0 suele significar que todo salió BIEN

mi_vm_ip = "192.168.150.97" # Cambia esto por una IP real de tu red
monitorear_con_detalle(mi_vm_ip)