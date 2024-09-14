import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QWidget

def leer_clave():
    app = QApplication(sys.argv)
    ventana = QWidget()
    ventana.setWindowTitle('Clave Secreta')
    
    layout = QVBoxLayout()
    clave_input = QLineEdit()
    clave_input.setEchoMode(QLineEdit.Password)  # Ocultar caracteres de la clave

    layout.addWidget(clave_input)
    ventana.setLayout(layout)
    ventana.resize(300, 100)
    ventana.show()
    sys.exit(app.exec_())

leer_clave()
