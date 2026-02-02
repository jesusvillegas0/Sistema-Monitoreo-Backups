import subprocess
import platform

infraestructura = {
    "Proxmox": "192.168.150.98",
    "Windows": "192.168.150.64",
    "VMware": "192.168.150.80"
}

def realizar_ping(nombre, ip):
    try:
        parametro = "-n" if platform.system().lower() == "windows" else "-c"
        comando = ["ping", parametro, "1", ip]
        
        print(f"Verificando {nombre} ({ip})...")
               
        resultado = subprocess.run(comando, stdout=subprocess.PIPE, text=True)
    
        if "TTL=" in resultado.stdout:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error tecnico al intentar ping a {nombre}: {e}")
        return False

print("--- INICIANDO ESCANEO DE RED ---")

contador = 0

for nombre, ip in infraestructura.items():
    esta_vivo = realizar_ping(nombre, ip)

    if esta_vivo:
        print(f"{nombre} esta ONLINE")
    else:
        print(f"{nombre} esta OFFLINE")
        contador += 1
if contador > 0:
    print(f"Se encontraron {contador} servidores caidos!!")        

print("--- ESCANEO FINALIADO ---")







