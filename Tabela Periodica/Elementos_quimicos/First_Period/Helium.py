from PyQt5.QtWidgets import *

class HelWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.grid_config()
        self.unitUI()
        self.set_layout()
        self.show()
        
    def set_appear(self):
        self.setWindowTitle("₂ He")
        self.resize(600, 400)
        self.move(300, 150)
        #======================================================================================================================
        # Criando o layout de grade
    def grid_config(self):
        self.layout = QGridLayout()
        #======================================================================================================================
        # Personalizando a grelha
        self.layout.setHorizontalSpacing(10)                  # Espaçamento horizontal
        self.layout.setVerticalSpacing(10)                    # Espaçamento vertical
        self.layout.setContentsMargins(20, 20, 20, 20)       # Margens da grelha
        
        
        
    def unitUI(self):
        
        self.layout.addWidget(QLabel("Nome: Hélio"), 0, 1)
        self.layout.addWidget(QLabel("Distribuição Eletrônica: 1s²"), 1, 1)
        self.layout.addWidget(QLabel('Protões/Eletrões: 2'),2, 1)
        self.layout.addWidget(QLabel('Uso: Utilizado na produção de amônia (NH₃), como combustível em células de hidrogênio e na síntese de diversos compostos químicos'),3, 1)
        
        
    def set_layout(self):
        # Definindo o layout para a janela
        self.setLayout(self.layout)