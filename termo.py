print("\n######### Calculadora de Temperatura #########")
print("Bienvenido !!")
opcion = input(
    "Presiona 1 C a F, Presiona 2 F a C: "
)

if opcion == "1":
    temp = float(input("Ingresa la temperatura a convertir: "))
    conversion = (temp * 9/5) + 32
    print(f"El cambio de la temperatura Celsius {temp} a Fahrenheit es {round(conversion, 2)}")

elif opcion == "2":
    temp = float(input("Ingresa la temperatura a convertir: "))
    conversion = (temp - 32) * 5/9
    print(f"El cambio de la temperatura Fahrenheit {temp} a Celsius es {round(conversion, 2)}")

else:
    print("Debe ingresar una temperatura correcta !!")

