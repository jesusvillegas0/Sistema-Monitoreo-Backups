import requests

url = "https://procuracenter.com.ve/"

print("---- Chequeando pagina Procura Center ----")
try:

    respuesta =  requests.get(url, timeout=15)

    if respuesta.status_code == 200:
        print("La pagina esta SALUDABLE")
    else:
        print(f"La pagina respondio con el siguiente codigo {respuesta.status_code}")
except requests.exceptions.ReadTimeout:
    print("ERROR DE DEVOPS: El servidor tardó demasiado en responder (Timeout).")
    # Aquí es donde dispararías la alerta que planeamos antes
except requests.exceptions.ConnectionError:
    print("ERROR DE RED: No se pudo conectar al servidor. ¿Está caído?")
except requests.exceptions.HTTPError:
    print("Ocurrió un error que no esperábamos")