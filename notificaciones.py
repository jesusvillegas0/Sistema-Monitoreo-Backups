from plyer import notification
import winsound

class Alerta:
    def lanzar_alerta(self, backup):
        #. Sonido: Frecuencia 1000Hz, Duracion 500ms
        winsound.Beep(500, 100)

        # Notificacion Visual
        notification.notify(
                "ALERTA DE BACKUPS",
                f"No se encontro el {backup}. Revisa!!!",
                app_name="Monitor de Red",
                timeout=5)