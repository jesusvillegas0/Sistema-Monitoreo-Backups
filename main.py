"""
# Conficional IF

SI se cumple esta condicion
    ejecutar grupo de instrucciones
SI NO:
    se ejecutan otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras instrucciones

# Operadores de comparacion
== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que


"""

# Ejemplo 1
print("\n############## EJEMPLO 1 ########################")

color = "rojo"
#color = input("Adivina cual es mi color favorito: ")

if color == "rojo":
    print("Enhorabuena!!")
    print("El color es ROJO")
else:
    print("El color incorrecto")

# Ejemplo 2
print("\n############## EJEMPLO 2 ########################")

year = 2025
#year = int(input("En que año estamos?: "))

if year < 2026:
    print("Estamos antes de 2026 en adelante !!")
else:
    print("Es un año posterior a 2026")

# Ejemplo 3
print("\n############## EJEMPLO 3 ########################")

nombre = "Jesus"