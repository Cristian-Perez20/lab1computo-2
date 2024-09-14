import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QFormLayout, QWidget

def leer_datos_personales():
    app = QApplication(sys.argv)
    ventana = QWidget()
    ventana.setWindowTitle('Datos Personales')

    layout = QFormLayout()
    
    cedula_input = QLineEdit()
    nombre_input = QLineEdit()

    layout.addRow('Número de cédula:', cedula_input)
    layout.addRow('Nombre completo:', nombre_input)

    ventana.setLayout(layout)
    ventana.resize(300, 150)
    ventana.show()
    sys.exit(app.exec_())

leer_datos_personales()
