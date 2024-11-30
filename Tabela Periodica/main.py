from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from __init__ import *
from inst import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.grid_config()
        self.initUI()
        self.elements_list()
        self.connects()
        self.set_layout()
    def set_appear(self):
        # Configuracoes de janela
        self.move(200, 100)
        self.resize(1200, 720)

        #======================================================================================================================
        # Criando o layout de grade
    def grid_config(self):
        self.layout = QGridLayout()
        #======================================================================================================================
        # Personalizando a grelha
        self.layout.setHorizontalSpacing(5)            # Espaçamento horizontal
        self.layout.setVerticalSpacing(5)              # Espaçamento vertical
        self.layout.setContentsMargins(15, 15, 15, 15)  # Margens da grelha
        #======================================================================================================================
    def initUI(self):
        self.lanthanides1 = QLabel('            *')
        self.actinides1 = QLabel('         **')
        
        self.lanthanides2 = QLabel('             *')
        self.actinides2 = QLabel('           **')        
        
        
        self.hydrogen = QPushButton("₁ H")
        self.helium = QPushButton("₂ He")
        self.lithium = QPushButton("₃ Li")
        self.beryllium = QPushButton("₄ Be")
        self.boron = QPushButton("₅ B")
        self.carbon = QPushButton("₆ C")
        self.nitrogen = QPushButton("₇ N")
        self.oxygen = QPushButton("₈ O")
        self.fluorine = QPushButton("₉ F")
        self.neon = QPushButton("₁₀ Ne")
        self.sodium = QPushButton("₁₁ Na")
        self.magnesium = QPushButton("₁₂ Mg")
        self.aluminum = QPushButton("₁₃ Al")
        self.silicon = QPushButton("₁₄ Si")
        self.phosphorus = QPushButton("₁₅ P")
        self.sulfur = QPushButton("₁₆ S")
        self.chlorine = QPushButton("₁₇ Cl")
        self.argon = QPushButton("₁₈ Ar")
        self.potassium = QPushButton("₁₉ K")
        self.calcium = QPushButton("₂₀ Ca")
        self.scandium = QPushButton("₂₁ Sc")
        self.titanium = QPushButton("₂₂ Ti")
        self.vanadium = QPushButton("₂₃ V")
        
        
        
        
        pass
    def elements_list(self):
        
        self.layout.addWidget(self.lanthanides1, 6, 3)
        self.layout.addWidget(self.actinides1, 7, 3)
        self.layout.addWidget(self.lanthanides2, 8, 1)
        self.layout.addWidget(self.actinides2, 9, 1)
        
        
        # Adicionando botões na grelha
        # 1 periodo
        self.layout.addWidget(self.hydrogen, 1, 1)
        self.layout.addWidget(self.helium, 1, 18)
        #======================================================================================================================
        # 2 periodo
        self.layout.addWidget(self.lithium, 2, 1)
        self.layout.addWidget(self.beryllium, 2, 2)
        self.layout.addWidget(self.boron, 2, 13)
        self.layout.addWidget(self.carbon, 2, 14)
        self.layout.addWidget(self.nitrogen, 2, 15)
        self.layout.addWidget(self.oxygen, 2, 16)
        self.layout.addWidget(self.fluorine, 2, 17)
        self.layout.addWidget(self.neon, 2, 18)
        #======================================================================================================================
        # 3 periodo
        self.layout.addWidget(self.sodium, 3, 1)
        self.layout.addWidget(self.magnesium, 3, 2)
        self.layout.addWidget(self.aluminum, 3, 13)
        self.layout.addWidget(self.silicon, 3, 14)
        self.layout.addWidget(self.phosphorus, 3, 15)
        self.layout.addWidget(self.sulfur, 3, 16)
        self.layout.addWidget(self.chlorine, 3, 17)
        self.layout.addWidget(self.argon, 3, 18)
        #======================================================================================================================
        # 4 periodo
        self.layout.addWidget(self.potassium, 4, 1)
        self.layout.addWidget(self.calcium, 4, 2)
        self.layout.addWidget(self.scandium, 4, 3)
        self.layout.addWidget(self.titanium, 4, 4)
        self.layout.addWidget(self.vanadium, 4, 5)
        self.layout.addWidget(QPushButton("₂₄ Cr"), 4, 6)
        self.layout.addWidget(QPushButton("₂₅ Mn"), 4, 7)
        self.layout.addWidget(QPushButton("₂₆ Fe"), 4, 8)
        self.layout.addWidget(QPushButton("₂₇ Co"), 4, 9)
        self.layout.addWidget(QPushButton("₂₈ Ni"), 4, 10)
        self.layout.addWidget(QPushButton("₂₉ Cu"), 4, 11)
        self.layout.addWidget(QPushButton("₃₀ Zn"), 4, 12)
        self.layout.addWidget(QPushButton("₃₁ Ga"), 4, 13)
        self.layout.addWidget(QPushButton("₃₂ Ge"), 4, 14)
        self.layout.addWidget(QPushButton("₃₃ As"), 4, 15)
        self.layout.addWidget(QPushButton("₃₄ Se"), 4, 16)
        self.layout.addWidget(QPushButton("₃₅ Br"), 4, 17)
        self.layout.addWidget(QPushButton("₃₆ Kr"), 4, 18)
        #======================================================================================================================
        # 5 periodo
        self.layout.addWidget(QPushButton("₃₇ Rb"), 5, 1)
        self.layout.addWidget(QPushButton("₃₈ Sr"), 5, 2)
        self.layout.addWidget(QPushButton("₃₉ Y"), 5, 3)
        self.layout.addWidget(QPushButton("₄₀ Zr"), 5, 4)
        self.layout.addWidget(QPushButton("₄₁ Nb"), 5, 5)
        self.layout.addWidget(QPushButton("₄₂ Mo"), 5, 6)
        self.layout.addWidget(QPushButton("₄₃ Tc"), 5, 7)
        self.layout.addWidget(QPushButton("₄₄ Ru"), 5, 8)
        self.layout.addWidget(QPushButton("₄₅ Rh"), 5, 9)
        self.layout.addWidget(QPushButton("₄₆ Pd"), 5, 10)
        self.layout.addWidget(QPushButton("₄₇ Ag"), 5, 11)
        self.layout.addWidget(QPushButton("₄₈ Cd"), 5, 12)
        self.layout.addWidget(QPushButton("₄₉ In"), 5, 13)
        self.layout.addWidget(QPushButton("₅₀ Sn"), 5, 14)
        self.layout.addWidget(QPushButton("₅₁ Sb"), 5, 15)
        self.layout.addWidget(QPushButton("₅₂ Te"), 5, 16)
        self.layout.addWidget(QPushButton("₅₃ I"), 5, 17)
        self.layout.addWidget(QPushButton("₅₄ Xe"), 5, 18)
        #======================================================================================================================
        # 6 periodo
        self.layout.addWidget(QPushButton("₅₅ Cs"), 6, 1)
        self.layout.addWidget(QPushButton("₅₆ Ba"), 6, 2)
        self.layout.addWidget(QPushButton("₅₇ La"), 8, 2)
        self.layout.addWidget(QPushButton("₅₈ Ce"), 8, 3)
        self.layout.addWidget(QPushButton("₅₉ Pr"), 8, 4)
        self.layout.addWidget(QPushButton("₆₀ Nd"), 8, 5)
        self.layout.addWidget(QPushButton("₆₁ Pm"), 8, 6)
        self.layout.addWidget(QPushButton("₆₂ Sm"), 8, 7)
        self.layout.addWidget(QPushButton("₆₃ Eu"), 8, 8)
        self.layout.addWidget(QPushButton("₆₄ Gd"), 8, 9)
        self.layout.addWidget(QPushButton("₆₅ Tb"), 8, 10)
        self.layout.addWidget(QPushButton("₆₆ Dy"), 8, 11)
        self.layout.addWidget(QPushButton("₆₇ Ho"), 8, 12)
        self.layout.addWidget(QPushButton("₆₈ Er"), 8, 13)
        self.layout.addWidget(QPushButton("₆₉ Tm"), 8, 14)
        self.layout.addWidget(QPushButton("₇₀ Yb"), 8, 15)
        self.layout.addWidget(QPushButton("₇₁ Lu"), 8, 16)
        self.layout.addWidget(QPushButton("₇₂ Hf"), 6, 4)
        self.layout.addWidget(QPushButton("₇₃ Ta"), 6, 5)
        self.layout.addWidget(QPushButton("₇₄ W"), 6, 6)
        self.layout.addWidget(QPushButton("₇₅ Re"), 6, 7)
        self.layout.addWidget(QPushButton("₇₆ Os"), 6, 8)
        self.layout.addWidget(QPushButton("₇₇ Ir"), 6, 9)
        self.layout.addWidget(QPushButton("₇₈ Pt"), 6, 10)
        self.layout.addWidget(QPushButton("₇₉ Au"), 6, 11)
        self.layout.addWidget(QPushButton("₈₀ Hg"), 6, 12)
        self.layout.addWidget(QPushButton("₈₁ Tl"), 6, 13)
        self.layout.addWidget(QPushButton("₈₂ Pb"), 6, 14)
        self.layout.addWidget(QPushButton("₈₃ Bi"), 6, 15)
        self.layout.addWidget(QPushButton("₈₄ Po"), 6, 16)
        self.layout.addWidget(QPushButton("₈₅ At"), 6, 17)
        self.layout.addWidget(QPushButton("₈₆ Rn"), 6, 18)
        #======================================================================================================================
        # 7 periodo
        self.layout.addWidget(QPushButton("₈₇ Fr"), 7, 1)
        self.layout.addWidget(QPushButton("₈₈ Ra"), 7, 2)
        self.layout.addWidget(QPushButton("₈₉ Ac"), 9, 2)
        self.layout.addWidget(QPushButton("₉₀ Th"), 9, 3)
        self.layout.addWidget(QPushButton("₉₁ Pa"), 9, 4)
        self.layout.addWidget(QPushButton("₉₂ U"), 9, 5)
        self.layout.addWidget(QPushButton("₉₃ Np"), 9, 6)
        self.layout.addWidget(QPushButton("₉₄ Pu"), 9, 7)
        self.layout.addWidget(QPushButton("₉₅ Am"), 9, 8)
        self.layout.addWidget(QPushButton("₉₆ Cm"), 9, 9)
        self.layout.addWidget(QPushButton("₉₇ Bk"), 9, 10)
        self.layout.addWidget(QPushButton("₉₈ Gf"), 9, 11)
        self.layout.addWidget(QPushButton("₉₉ Es"), 9, 12)
        self.layout.addWidget(QPushButton("₁₀₀ Fm"), 9, 13)
        self.layout.addWidget(QPushButton("₁₀₁ Md"), 9, 14)
        self.layout.addWidget(QPushButton("₁₀₂ No"), 9, 15)
        self.layout.addWidget(QPushButton("₁₀₃ Lr"), 9, 16)
        self.layout.addWidget(QPushButton("₁₀₄ Rf"), 7, 4)
        self.layout.addWidget(QPushButton("₁₀₅ Db"), 7, 5)
        self.layout.addWidget(QPushButton("₁₀₆ Sg"), 7, 6)
        self.layout.addWidget(QPushButton("₁₀₇ Bh"), 7, 7)
        self.layout.addWidget(QPushButton("₁₀₈ Hs"), 7, 8)
        self.layout.addWidget(QPushButton("₁₀₉ Mt"), 7, 9)
        self.layout.addWidget(QPushButton("₁₁₀ Ds"), 7, 10)
        self.layout.addWidget(QPushButton("₁₁₁ Rg"), 7, 11)
        self.layout.addWidget(QPushButton("₁₁₂ Cn"), 7, 12)
        self.layout.addWidget(QPushButton("₁₁₃ Nh"), 7, 13)
        self.layout.addWidget(QPushButton("₁₁₄ Fl"), 7, 14)
        self.layout.addWidget(QPushButton("₁₁₅ Mc"), 7, 15)
        self.layout.addWidget(QPushButton("₁₁₆ Lv"), 7, 16)
        self.layout.addWidget(QPushButton("₁₁₇ Ts"), 7, 17)
        self.layout.addWidget(QPushButton("₁₁₈ Og"), 7, 18)
        #======================================================================================================================
    def connects(self):
        self.hydrogen.clicked.connect(self.hydrogen1)
        self.helium.clicked.connect(self.helium2)
        self.lithium.clicked.connect(self.lithium3)
        self.beryllium.clicked.connect(self.beryllium4)
        self.boron.clicked.connect(self.boron5)
        self.carbon.clicked.connect(self.carbon6)
        self.nitrogen.clicked.connect(self.nitrogen7)
        self.oxygen.clicked.connect(self.oxygen8)
        self.fluorine.clicked.connect(self.fluorine9)
        self.neon.clicked.connect(self.neon10)
        self.sodium.clicked.connect(self.sodium11)
        self.magnesium.clicked.connect(self.magnesium12)
        self.aluminum.clicked.connect(self.aluminum13)
        self.silicon.clicked.connect(self.silicon14)
        self.phosphorus.clicked.connect(self.phosphorus15)
        self.sulfur.clicked.connect(self.sulfur16)
        self.chlorine.clicked.connect(self.chlorine17)
        self.argon.clicked.connect(self.argon18)
        self.potassium.clicked.connect(self.potassium19)
        self.calcium.clicked.connect(self.calcium20)
        self.scandium.clicked.connect(self.scandium21)
        self.titanium.clicked.connect(self.titanium22)
        self.vanadium.clicked.connect(self.vanadium23)
        
        
    def hydrogen1(self):
        self.hydrogen = HydWin()
        self.hydrogen.show()
        
    def helium2(self):
        self.helium = HelWin()
        self.helium.show()

    def lithium3(self):
        self.lithium = LitWin()
        self.lithium.show()
        
    def beryllium4(self):
        self.beryllium = BerWin()
        self.beryllium.show()
    
    def boron5(self):
        self.boron = BorWin()
        self.boron.show()
        
    def carbon6(self):
        self.carbon = CarWin()
        self.carbon.show()
        
    def nitrogen7(self):
        self.nitrogen = NitWin()
        self.nitrogen.show()
        
    def oxygen8(self):
        self.oxygen = OxyWin()
        self.oxygen.show()
        
    def fluorine9(self):
        self.fluorine = FluWin()
        self.fluorine.show()
        
    def neon10(self):
        self.neon = NeoWin()
        self.neon.show()
        
    def sodium11(self):
        self.sodium = SodWin()
        self.sodium.show()
        
    def magnesium12(self):
        self.magnesium = MagWin()
        self.magnesium.show()
        
    def aluminum13(self):
        self.aluminum = AluWin()
        self.aluminum.show()
        
    def silicon14(self):
        self.silicon = SilWin()
        self.silicon.show()
        
    def phosphorus15(self):
        self.phosphorus = PhoWin()
        self.phosphorus.show()
        
    def sulfur16(self):
        self.sulfur = SulWin()
        self.sulfur.show()
        
    def chlorine17(self):
        self.chlorine = ChlWin()
        self.chlorine.show()
        
    def argon18(self):
        self.argon = ArgWin()
        self.argon.show()
        
    def potassium19(self):
        self.potassium = PotWin()
        self.potassium.show()
        
    def calcium20(self):
        self.calcium = CalWin()
        self.calcium.show()
        
    def scandium21(self):
        self.scandium = ScaWin()
        self.scandium.show()
        
    def titanium22(self):
        self.titanium = TitWin()
        self.titanium.show()
        
    def vanadium23(self):
        self.vanadium = VanWin()
        self.vanadium.show()
        
        
    def set_layout(self):
        # Definindo o layout para a janela
        self.setLayout(self.layout)
        self.setWindowTitle("Tabela periodica")
        #======================================================================================================================


# Inicializando o aplicativo
app = QApplication([])
window = MainWin()
window.show()
app.exec_()