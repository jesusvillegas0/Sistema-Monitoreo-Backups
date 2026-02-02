import requests # El motor para conectarnos a internet

class MonitorInfraestructura:
    def __init__(self, url):
        self.url = url
        self.estado_servicio = "Desconocido"

    def realizar_health_check(self):
        print(f"🔍 Iniciando Health Check en: {self.url}...")
        
        try:
            # Intentamos conectarnos (con un tiempo límite de 5 segundos)
            respuesta = requests.get(self.url, timeout=5)
            
            # Verificamos el código de estado (200 es éxito)
            if respuesta.status_code == 200:
                self.estado_servicio = "SALUDABLE"
                datos = respuesta.json() # Convertimos la respuesta en un diccionario/lista
                
                print("✅ Conexión Exitosa.")
                print(f"📊 Reporte: Se encontraron {len(datos)} registros activos en la base de datos.")
                return datos
            else:
                self.estado_servicio = "FALLIDO"
                print(f"🚨 Alerta: El servidor respondió con error {respuesta.status_code}")
                
        except requests.exceptions.ConnectionError:
            print("❌ Error Crítico: No se pudo establecer conexión. ¿El servidor está caído?")
        except requests.exceptions.Timeout:
            print("⏳ Error: El servidor tardó demasiado en responder (Timeout).")
        except Exception as e:
            print(f"⚠️ Error inesperado: {e}")

    def generar_log_devops(self):
        # Aplicamos lo que aprendiste de archivos para guardar el resultado
        with open("server_logs.txt", "a") as log: # "a" de append (añadir al final sin borrar)
            from datetime import datetime
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.write(f"[{fecha}] URL: {self.url} | Estado: {self.estado_servicio}\n")
        print("📁 Resultado guardado en server_logs.txt")

# --- SIMULACIÓN DE EJECUCIÓN ---
url_produccion = "https://jsonplaceholder.typicode.com/users"
mi_monitor = MonitorInfraestructura(url_produccion)

# 1. Checamos la salud
usuarios = mi_monitor.realizar_health_check()

# 2. Si hay usuarios, mostramos el nombre de los primeros 3 (como un log de auditoría)
if usuarios:
    print("\n--- Auditoría de Usuarios ---")
    for u in usuarios[:3]:
        print(f"ID: {u['id']} | Usuario: {u['username']} | Email: {u['email']}")

# 3. Guardamos el registro del día
mi_monitor.generar_log_devops()

