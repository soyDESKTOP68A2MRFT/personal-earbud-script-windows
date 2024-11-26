import sys
import subprocess
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class BluetoothApp(QWidget):
    def __init__(self):
        super().__init__()

        # Configurar la ventana
        self.setWindowTitle('Control Audífonos Bluetooth')
        self.setGeometry(100, 100, 400, 200)

        # Crear widgets
        self.message_label = QLabel("Presiona para sincronizar", self)
        self.sync_button = QPushButton("Sincronizar Audífonos", self)
        self.connect_button = QPushButton("Conectar Audífonos", self)
        self.disconnect_button = QPushButton("Desconectar Audífonos", self)

        # Conectar los botones a las funciones
        self.sync_button.clicked.connect(self.on_sync_clicked)
        self.connect_button.clicked.connect(self.on_connect_clicked)
        self.disconnect_button.clicked.connect(self.on_disconnect_clicked)

        # Crear el layout y agregar los widgets
        layout = QVBoxLayout()
        layout.addWidget(self.message_label)
        layout.addWidget(self.sync_button)
        layout.addWidget(self.connect_button)
        layout.addWidget(self.disconnect_button)

        self.setLayout(layout)

    def run_bat_script(self, action):
        """ Ejecutar el archivo .bat con la acción proporcionada """
        try:
            result = subprocess.run(["control_audifonos.bat", action], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}"

    def on_sync_clicked(self):
        """ Sincronizar los audífonos """
        result = self.run_bat_script("sync")
        self.message_label.setText(result)

    def on_connect_clicked(self):
        """ Conectar los audífonos """
        result = self.run_bat_script("connect")
        self.message_label.setText(result)

    def on_disconnect_clicked(self):
        """ Desconectar los audífonos """
        result = self.run_bat_script("disconnect")
        self.message_label.setText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BluetoothApp()
    window.show()
    sys.exit(app.exec())
