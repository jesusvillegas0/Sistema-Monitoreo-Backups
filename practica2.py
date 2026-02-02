infraestructura = {
    "Proxmox": "192.168.150.4",
    "Windows": "192.168.150.6",
    "VMware": "192.168.150.3"
}

def mostrar_datos(nombre_servidor, ip_servidor):
    print(f"El servidor {nombre_servidor} tiene la direccion IP {ip_servidor}")

    
for nombre, ip in infraestructura.items():
    mostrar_datos(nombre, ip)



    