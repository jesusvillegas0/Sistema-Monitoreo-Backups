class Auto:
    # El constructor define qué "partes" tiene el objeto al nacer
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self._precio = precio
        self.encendido = False
        self.frenos = False

    # Método para ver el precio (Getter)
    def mostrar_precio(self):
        return self._precio
    
    # Método para modificar el precio con reglas (Setter)
    def establecer_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self._precio = nuevo_precio
            print(f"Precio actualizado a: ${self._precio}")
        else:
            print("Error: El precio debe ser mayor a 0.")

    # Un método es una "acción" que el objeto puede hacer
    def arrancar(self):
        self.encendido = True
        return f"El {self.marca} ha arrancado. ¡Brum brum!"
    
    def frenar(self):
        self.frenos = True
        return f"El {self.marca} se ha detenido!!"
    
    def aplicar_descuento(self, porcentaje):
        descuento = self._precio * (porcentaje / 100)
        self._precio = self._precio - descuento

        return f"Nuevo precio aplicado: ${self._precio}"
    
class Camion(Auto): # Al poner Auto entre paréntesis, Camion HEREDA todo
    def __init__(self, marca, modelo, precio, carga_maxima):
        # super() llama al constructor del padre (Auto)
        super().__init__(marca, modelo, precio)
        self.carga_maxima = carga_maxima

    def cargar(self):
        return f"Cargando {self.carga_maxima} toneladas..."
    
    def arrancar(self): # Reescribimos el método del padre
        self.encendido = True
        return f"¡RUMMM! El potente motor del camión {self.marca} está listo para la carga."

class Concesionario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_vehiculos = []

    def agregar(self, v):
        self.lista_vehiculos.append(v)
        print(f"--- Registrado: {v.marca} ---")

    def mostrar_todo(self):
        print(f"\nCATÁLOGO DE {self.nombre.upper()}")
        for i, v in enumerate(self.lista_vehiculos):
            tipo = "Camión" if isinstance(v, Camion) else "Auto"
            print(f"[{i}] {tipo}: {v.marca} {v.modelo} | Precio: ${v.mostrar_precio()}")

    def gestionar_descuento(self):
        self.mostrar_todo()
        try:
            indice = int(input("\nSelecciona el número del vehículo para aplicar descuento: "))
            # Validamos que el índice exista en la lista
            if 0 <= indice < len(self.lista_vehiculos):
                vehiculo = self.lista_vehiculos[indice]
                
                confirmar = input(f"¿Quieres aplicar un descuento al {vehiculo.modelo}? (s/n): ").lower()
                if confirmar == 's':
                    porcentaje = float(input("¿De cuánto será el porcentaje de descuento? (ej. 10): "))
                    # Llamamos al método del objeto y guardamos el mensaje que devuelve
                    mensaje = vehiculo.aplicar_descuento(porcentaje)
                    print(f"✅ {mensaje}")
                else:
                    print("Operación cancelada.")
            else:
                print("❌ Número de vehículo no válido.")
        except ValueError:
            print("❌ Por favor, ingresa solo números.")

      

    def preparar_para_venta(self):
        print(f"\n--- Poniendo a punto los vehículos en {self.nombre} ---")
        for v in self.lista_vehiculos:
            print(v.arrancar())
            print(v.frenar())
            # Aplicamos un bono de bienvenida
            v.aplicar_descuento(5)

    # Dentro de la clase Concesionario:
    def generar_reporte_archivo(self):
        try:

            with open("reporte_inventario.txt", "w") as archivo:
                archivo.write(f"REPORTE DE {self.nombre}\n")
                archivo.write("========================\n")
                for v in self.lista_vehiculos:
                    linea = f"Vehículo: {v.marca} {v.modelo} - Precio: {v.mostrar_precio()}\n"
                    archivo.write(linea)
            print("📂 Reporte generado exitosamente en 'reporte_inventario.txt'")
        except IOError as e:
            print(f"❌ Error de entrada/salida: No se pudo escribir el archivo. {e}")
        except Exception as e:
            print(f"⚠️ Ocurrió un error inesperado: {e}")

