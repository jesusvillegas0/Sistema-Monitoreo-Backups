from base_datos import BaseDatos

def menu():
    db = BaseDatos("backups_sistema.db")

    while True:
        print("\n--- PANEL DE CONTROL DE BACKUPS ---")
        print("1. Ver servidores monitoreados")
        print("2. Agregar nuevo servidor")
        print("3. Eliminar servidor")
        print("4. Actualizar")
        print("5. Salir")

        opcion = input("\nSelecciona una opcion: ")

        if opcion == "1":
            db.consultar_servidores()
        elif opcion == "2":
            db.agregar_servidor_interativo()
        elif opcion == "3":
            print("--- Listado de los servidores ---")
            db.consultar_servidores()
            id_borrar = input("\nIngresa el ID del servidor a borrar: ")
            confirmacion = input(f"Estas seguro que quieres borrar el servidor con el ID {id_borrar}? Yes/No: ").capitalize()
            if confirmacion == "Yes":
                db.eliminar_servidor(id_borrar)
            else:
                print("Acción cancelada. Volviendo al menú principal...")
        elif opcion == "4":
            print("--- Listado de los servidores ---")
            db.consultar_servidores()
            id_act = input("\nIngresa el ID a actualizar: ")
            nuevo_nombre = input("\nIngresa el nuevo nombre: ")
            nueva_ruta = input("\nIngresa la nueva ruta (ej. \\192.168...): ")
            nuevo_prefijo = input("\nIngresa el nuevo prefijo: ")
            nuevo_formato = input("\nIngresa el nuevo formato: ")

            db.actualizar_servidor(id_act, nuevo_nombre, nueva_ruta, nuevo_prefijo, nuevo_formato)

        elif opcion == "5":
            print("Saliendo del panel...")
            break
        else:
            print("Opcion no valida")
if __name__ == "__main__":
    menu()