from base_datos import BaseDatos

def menu():
    db = BaseDatos("backups_sistema.db")

    while True:
        print("\n--- PANEL DE CONTROL DE BACKUPS ---")
        print("1. Ver servidores monitoreados")
        print("2. Agregar nuevo servidor")
        print("3. Eliminar servidor")
        print("4. Salir")

        opcion = input("\nSelecciona una opcion: ")

        if opcion == "1":
            db.consultar_servidores()
        elif opcion == "2":
            db.agregar_servidor_interativo()
        elif opcion == "3":
            print("--- Listado de los servidores ---")
            db.consultar_servidores()
            id_borrar = input("\nIntroduce el ID del servidor a borrar: ")
            confirmacion = input(f"Estas seguro que quieres borrar el servidor con el ID {id_borrar}? Yes/No: ").capitalize()
            if confirmacion == "Yes":
                db.eliminar_servidor(id_borrar)
            else:
                print("Acción cancelada. Volviendo al menú principal...")

        elif opcion == "4":
            print("Saliendo del panel...")
            break
        else:
            print("Opcion no valida")
if __name__ == "__main__":
    menu()