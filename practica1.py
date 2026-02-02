intentos = 0
password = "Odin123"

while True:    
    usuario =  input("\nIngresa tu usuario?: ")
    clave = input("Ingresa tu contraseña: ")

    if usuario.capitalize() == "Bebe" and clave == password:
        print("\nAcceso Total al Clúster. ¡Bienvenida!")
        break
    else:
        intentos += 1
        print("\nError de autenticación. Acceso denegado.")
        if intentos > 0 and intentos <=2:
            print(f"Te quedan {3 - intentos} intentos !!")
    if intentos >= 3:
        print("\nCuenta bloqueada por seguridad!!")
        break
