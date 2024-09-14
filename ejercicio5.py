import sys
from PyQt5.QtWidgets import QApplication, QFormLayout, QLineEdit, QWidget

def leer_datos_persona():
    app = QApplication(sys.argv)
    ventana = QWidget()
    ventana.setWindowTitle('Datos Característicos')

    layout = QFormLayout()
    
    datos = ['Nombre', 'Edad', 'Número de cédula', 'Dirección', 'Teléfono', 'Correo electrónico', 'Altura', 'Peso', 'Nacionalidad', 'Profesión']
    for dato in datos:
        input_field = QLineEdit()
        layout.addRow(dato + ':', input_field)

    ventana.setLayout(layout)
    ventana.resize(400, 500)
    ventana.show()
    sys.exit(app.exec_())

leer_datos_persona()
