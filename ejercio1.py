import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def mostrar_datos():
    app = QApplication(sys.argv)
    ventana = QWidget()
    ventana.setWindowTitle('Datos Personales')
    
    layout = QVBoxLayout()

    nombre_label = QLabel('Nombre: Cristian Pérez')
    edad_label = QLabel('Edad: 20')

    nombre_label.setAlignment(Qt.AlignCenter)
    edad_label.setAlignment(Qt.AlignCenter)

    layout.addWidget(nombre_label)
    layout.addWidget(edad_label)

    ventana.setLayout(layout)
    ventana.resize(300, 100)
    ventana.show()
    sys.exit(app.exec_())

mostrar_datos()
