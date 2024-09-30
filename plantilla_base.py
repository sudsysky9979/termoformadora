__author__ = "Angel"

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel ##aplicaciones, ventana
from PyQt6.QtGui import QFont,QPixmap ##importar tipo de letra
from PyQt6.QtCore import Qt ##banderas para alinear
import sys
from pathlib import Path

def abs_path(ruta:str):
    return str(Path(__file__).parent.absolute() / ruta)

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Procesador de cocos") ##nombre principal de ventana
        print (__file__)

        titulo=QLabel("Hola, bienvenido")
        fuente = QFont("manjari", 24)
        titulo.setFont(fuente)
        ##titulo.setAlignment(Qt.AlignmentFlag.AlignHCenter\
        ##                    | Qt.AlignmentFlag.AlignVCenter)## alineacion horizontal centrada y alineacion vertical centrada
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)## alinear en una sola en horizontal y vertical
        imagen = QPixmap(abs_path("../../images/ctulhu.jpeg"))
        titulo.setPixmap(imagen)
        titulo.setScaledContents(True)

        self.setCentralWidget(titulo)
        
        ##self.setFixedSize(300, 100) ##se queda fijo el tamaño de ventana
        self.resize(300, 100) ##se puede modificar el tamaño de ventana 

def main ():
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 


