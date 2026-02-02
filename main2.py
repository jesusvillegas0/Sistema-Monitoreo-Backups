from vehiculo import Auto, Camion, Concesionario # Aquí importamos tu módulo

tienda = Concesionario("Super Autos")

# Creamos objetos reales basados en el plano
mi_auto = Auto("Toyota","Corolla", 25000)
"""
print(f"Tengo un {mi_auto.marca} que cuesta ${mi_auto.precio}")
print(mi_auto.arrancar())
mi_auto.aplicar_descuento(30)

print(f"Con el descuento el precio es: ${mi_auto.precio}")
print(mi_auto.frenar())
"""
mi_camion = Camion("Ford", "F750", 300000, "15")
mi_camion_grande = Camion("Chevrolet", "Toronto", 250000, "30")
"""
print(f"\nTengo a hora un camion {mi_camion.marca} que cuesta ${mi_camion.precio}")
print(mi_camion.arrancar())
print(mi_camion.cargar())
mi_camion.aplicar_descuento(25)

print(f"Con el descuento el precio es: ${mi_camion.precio}")

"""
tienda.agregar(mi_auto)
tienda.agregar(mi_camion)
tienda.agregar(mi_camion_grande)

tienda.gestionar_descuento()

tienda.mostrar_todo()
tienda.generar_reporte_archivo()