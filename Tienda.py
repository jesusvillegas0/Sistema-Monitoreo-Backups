
def calcular_iva(monto):
    impuesto = 0.16 * monto
    return impuesto

precios = {
    "manzana": 1.50,
    "pan": 0.80,
    "leche": 1.10,
    "harina": 0.90,
    "pasta": 2
}

total_cuenta = 0

while True:
    print("\n--- Tienda Virtual ---")
    print("1. Ver Inventario")
    print("2. Buscar Producto")
    print("3. Agregar/Actualizar")
    print("4. Comprar")
    print("5. Salir")

    opcion = input("\nElige una opción: ")
    
    if opcion == "1":
        print("\n########## INVENTARIO ###############")
        for nombre, precio in precios.items():
            print(f"- {nombre} - ${precio}")
    elif opcion == "2":
        buscar = input("¿Qué buscas?: ")
        if buscar in precios:
            print(f"\nEl precio es {precios[buscar]}")
        else:
            print("\nEse producto no está en el inventario.")

    elif opcion == "3":
        nuevo_nombre = input("Nombre del producto: ").lower()
        try:
            nuevo_precio = float(input(f"Ingresa el precio para {nuevo_nombre}: "))

            precios[nuevo_nombre] = nuevo_precio
            print(f"\n{nuevo_nombre} Guardado con exito !!!")
            print(f"El nuevo precio de {nuevo_nombre} es {nuevo_precio}")
        except ValueError:
            print("Error: El precio debe ser un número.")

    elif opcion == "4":
        articulo = input("Que deseas comprar?: ").lower()
        if articulo in precios:
            try:
                cantidad = int(input(f"Que cantidad del articulo {articulo} deseas?: "))
                pago = precios[articulo] * cantidad
                total_cuenta += pago
                print(f"Subtotal a pagar: ${round(pago, 2)}")
                print(f"Llevas acumulado: ${round(total_cuenta, 2)}")
            except ValueError:
                print("Solo se aceptan numeros.")

    elif opcion == "5":
        iva_calculado = calcular_iva(total_cuenta)
        total_final = total_cuenta + iva_calculado
        print(f"Subtotal: ${round(total_cuenta, 2)}")
        print(f"IVA 16%: ${round(iva_calculado, 2)}")
        print(f"Total a pagar: ${round(total_final, 2)}")
        print(f"Gracias por su compra, su total fue: ${round(total_final, 2)}")
        print("\nAdios !!")
        break 
    else:
        print("\nDebes seleccionar una opcion valida!!")