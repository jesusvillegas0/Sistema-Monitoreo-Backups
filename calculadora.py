print("\n######### Calculadora de Temperatura #########")
print("Bienvenido !!")

def pedir_temperatura():
    try:
        numero = float(input("\nIngresa la temperatura a convertir: "))
        return numero
    except ValueError:
        print("\n¡Error! Debes ingresar un número válido.")
        return None

historial = []

while True:
    opcion = input(
    "\nPresiona 1 C a F, Presiona 2 F a C, Presiona 3: Historial o Salir: ")
        
    if opcion == "1" or opcion == "2":
        temp = pedir_temperatura()        
        if temp is not None:
            if opcion == "1":
                conversion = (temp * 9/5) + 32
                res = f"{temp}°C -> {round(conversion, 2)}°F"
            else:
                conversion = (temp - 32) * 5/9
                res = f"{temp}°F -> {round(conversion, 2)}°C"
            historial.append(res)
            print(f"\nResultado {res}")
           
    elif opcion == "3":
        print("\n--- Historial de Conversiones ---")
        if not historial:        
            print("El historial esta vacio")
        else:
            for registro in historial:
                print(registro)
        print("---------------------------------")

    
    elif opcion.capitalize() == "Salir":
        print("Adios !!")
        break   
    else:
        print("Ingresa una opcion correcta !!")
