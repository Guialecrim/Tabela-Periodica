from PyQt5.QtWidgets import *

class PotWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.grid_config()
        self.unitUI()
        self.set_layout()
        self.show()
        
    def set_appear(self):
        self.setWindowTitle("₁₉ K")
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
        self.layout.setContentsMargins(20, 20, 20, 20)        # Margens da grelha
        
        
        
    def unitUI(self):
        
        self.layout.addWidget(QLabel("Nome: Potássio"), 0, 1)
        self.layout.addWidget(QLabel('Distribuição Eletrônica: 1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹'), 1, 1)
        self.layout.addWidget(QLabel('Protões/Eletrões: 19'),2, 1)
        self.layout.addWidget(QLabel('Uso: Utilizado em fertilizantes, como sal dietético e em processos industriais'),3, 1)
        
        
    def set_layout(self):
        # Definindo o layout para a janela
        self.setLayout(self.layout)