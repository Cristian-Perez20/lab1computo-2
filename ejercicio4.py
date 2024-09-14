import sys
from PyQt5.QtWidgets import QApplication, QFormLayout, QLineEdit, QWidget

def leer_mascotas():
    app = QApplication(sys.argv)
    ventana = QWidget()
    ventana.setWindowTitle('Datos de Mascotas')

    layout = QFormLayout()
    
    for i in range(1, 4):
        nombre_input = QLineEdit()
        especie_input = QLineEdit()
        edad_input = QLineEdit()

        layout.addRow(f'Nombre Mascota {i}:', nombre_input)
        layout.addRow(f'Especie Mascota {i}:', especie_input)
        layout.addRow(f'Edad Mascota {i}:', edad_input)

    ventana.setLayout(layout)
    ventana.resize(300, 300)
    ventana.show()
    sys.exit(app.exec_())

leer_mascotas()
