import neural_net, prepare, neural_net, db
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout
from PyQt5 import QtCore
from numpy import exp, array, delete, swapaxes, add, matmul
from tkinter import messagebox as msb

#[56,	9.1,	0,	0.3,	0.5,	0.6,	20,	20,	30,	1.1,	6.4,	1.6,	0,	2.5,	0,	0]
#[56,	9.1,	0,	0.3,	0.5,	0.6,	20,	20,	30,	1.1,	0,	0]
#date = [56,	9.1,	0,	0.3,	0.5,	0.6,	20,	20,	30,	1.1,	6.4,	1.6,	0,	2.5,	0,	0]  # input by users

class App_(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.interfejs()
        
    def interfejs(self):
        # etykiety
        head = "Metoda oceny zagrożenia obwałami i opadem skał stropowych\nopracowana dla warunków polskich kopalń rud miedzi\n 2022"
        naHead = QLabel(head)
        naHead.setFont(QFont("Arial", 14, QFont.Bold))
        naHead.setAlignment(QtCore.Qt.AlignRight)
        ukladHe = QGridLayout()
        ukladHe.addWidget(naHead, 0, 0)
        naCz1OP = "<b>Czynniki geologiczne:</b><br>nr 1 Rodzaj skał stropowych"
        naCz2OP = "nr 2 - Wytrzymałość na rozciąganie"
        naCz3OP = "nr 3 - Spękania pionowe"
        naCz4OP = "nr 4 - Zawodnienie"
        naCz5OP = "nr 5 - Płaszczyzny osłabienia"
        naCz6OP = "nr 6 - Występowanie zaburzeń zalegania złoża "
        naCz7OP = "<b>Czynniki górnicze:</b><br>nr 7 - Średni postęp miesięczny frontu"
        naCz8OP = "nr 8 - Średni postęp mieś. likwidacji"
        naCz9OP = "nr 9 - Występowanie zaszłości (stare wyrobiska, zroby)"
        naCz10OP = "nr 10 - Głębokość zalegania złoża"
        naCz11OP = "<b>Czynniki techniczne:</b><br>nr 11 - Szerokość wyrobiska przy stropie"
        naCz12OP = "nr 12 - Długość kotwi"
        naCz13OP = "nr 13 - Dodatkowa obudowa"
        naCz14OP = "nr 14 - Czas istnienia wyrobiska"
        naCz15OP = "<b>Czynniki monitoring:</b><br>nr 15 - Opadnięcia elementów SRS"
        naCz16OP = "nr 16 - Rozwarstwienia stwierdzone badaniem endoskopowym"
        opis1OP = "1 –  Jednorodne piaskowce\n2 – Wapienie\n3 – Dolomity\n4 – Dolomit wapnisty o podzielności płytowej\n5 – Dolomit smugowany\n6 – Dolomit wapnisty\n7 – Dolomit ilasty"
        opis2OP = "<i>Wartość w MPa"
        opis3OP = "1 – Spękania pionowe\n0,5 – Spękania wypełnione substancją mineralną\n0 – Brak spękań"
        opis4OP = "1 – Stały wypływ\n0,6 – Wykroplenia\n0,3 – Wilgotne skały\n0 – Brak wody"
        opis5OP = "0,5 – płaszczyzna osłabienia w strefie kotwienia\n0 – strefa kotwienia obejmuje masywny strop"
        opis6OP = "1 – Uskok w obrębie poligonu\n0,6 – Lustro tektoniczne\n0,5 – Rejon o rozwiniętej mikrotektonice\n0,4 – Uskok w sąsiednich parcelach"
        opis7OP = "<i>Wartość w metrach na miesiąc</i>"
        opis8OP = "<i>Wartość w metrach na miesiąc</i>"
        opis9OP = "<i>Wartość w metrach liczonych do najbliższej  zaszłości</i>"
        opis10OP = "<i>Wartość w kilometrach</i>"
        opis11OP = "<i>Wartość w metrach</i>"
        opis12OP = "<i>Wartość w metrach</i>"
        opis13OP = "0 – brak; 1 – HT;  2 –  HT×2;  3 – SP\n4 – KLS; 5 – inne;  6 – SZ"
        opis14OP = "<i>Wartość w miesiącach</i>"
        opis15OP = "1 – Opadnięcie elementu SRS w parceli po wstrząsie\n0,5 – Opadnięcia elementu SRS w przyległych parcelach\n0,25 – Opadnięcia elementów SRS w polu\n0 – Brak opadnięć elementów SRS"
        opis16OP = "<i>Wartość w metrach</i>"
        naCz1 = QLabel(naCz1OP)
        naCz2 = QLabel(naCz2OP)
        naCz3 = QLabel(naCz3OP)
        naCz4 = QLabel(naCz4OP)
        naCz5 = QLabel(naCz5OP)
        naCz6 = QLabel(naCz6OP)
        naCz7 = QLabel(naCz7OP)
        naCz8 = QLabel(naCz8OP)
        naCz9 = QLabel(naCz9OP)
        naCz10 = QLabel(naCz10OP)
        naCz11 = QLabel(naCz11OP)
        naCz12 = QLabel(naCz12OP)
        naCz13 = QLabel(naCz13OP)
        naCz14 = QLabel(naCz14OP)
        naCz15 = QLabel(naCz15OP)
        naCz16 = QLabel(naCz16OP)
        opis1 = QLabel(opis1OP)
        opis2 = QLabel(opis2OP)
        opis3 = QLabel(opis3OP)
        opis4 = QLabel(opis4OP)
        opis5 = QLabel(opis5OP)
        opis6 = QLabel(opis6OP)
        opis7 = QLabel(opis7OP)
        opis8 = QLabel(opis8OP)
        opis9 = QLabel(opis9OP)
        opis10 = QLabel(opis10OP)
        opis11 = QLabel(opis11OP)
        opis12 = QLabel(opis12OP)
        opis13 = QLabel(opis13OP)
        opis14 = QLabel(opis14OP)
        opis15 = QLabel(opis15OP)
        opis16 = QLabel(opis16OP)
        self.warCz1 = QLineEdit()
        self.warCz2 = QLineEdit()
        self.warCz3 = QLineEdit()
        self.warCz4 = QLineEdit()
        self.warCz5 = QLineEdit()
        self.warCz6 = QLineEdit()
        self.warCz7 = QLineEdit()
        self.warCz8 = QLineEdit()
        self.warCz9 = QLineEdit()
        self.warCz10 = QLineEdit()
        self.warCz11 = QLineEdit()
        self.warCz12 = QLineEdit()
        self.warCz13 = QLineEdit()
        self.warCz14 = QLineEdit()
        self.warCz15 = QLineEdit()
        self.warCz16 = QLineEdit()
        naCz1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
        naCz2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
        naCz3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
        naCz4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
        naCz5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
        naCz6.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
        naCz7.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
        naCz8.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
        naCz9.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
        naCz10.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
        naCz11.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
        naCz12.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
        naCz13.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
        naCz14.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
        naCz15.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
        naCz16.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
        self.warCz1.setStyleSheet("background-color: #FF7645")
        self.warCz2.setStyleSheet("background-color: #FF7645")
        self.warCz3.setStyleSheet("background-color: #FF7645")
        self.warCz4.setStyleSheet("background-color: #FF7645")
        self.warCz5.setStyleSheet("background-color: #FF7645")
        self.warCz6.setStyleSheet("background-color: #FF7645")
        self.warCz7.setStyleSheet("background-color: #FF8214")
        self.warCz8.setStyleSheet("background-color: #FF8214")
        self.warCz9.setStyleSheet("background-color: #FF8214")
        self.warCz10.setStyleSheet("background-color: #FF8214")
        self.warCz11.setStyleSheet("background-color: #FF930F")
        self.warCz12.setStyleSheet("background-color: #FF930F")
        self.warCz13.setStyleSheet("background-color: #FF930F")
        self.warCz14.setStyleSheet("background-color: #FF930F")
        self.warCz15.setStyleSheet("background-color: #FFAA0D")
        self.warCz16.setStyleSheet("background-color: #FFAA0D")
        ukladT = QGridLayout()
        ukladT.addWidget(naCz1, 1, 0)
        ukladT.addWidget(naCz2, 2, 0)
        ukladT.addWidget(naCz3, 3, 0)
        ukladT.addWidget(naCz4, 4, 0)
        ukladT.addWidget(naCz5, 5, 0)
        ukladT.addWidget(naCz6, 6, 0)
        ukladT.addWidget(naCz7, 7, 0)
        ukladT.addWidget(naCz8, 8, 0)
        ukladT.addWidget(naCz9, 9, 0)
        ukladT.addWidget(naCz10, 10, 0)
        ukladT.addWidget(naCz11, 11, 0)
        ukladT.addWidget(naCz12, 12, 0)
        ukladT.addWidget(naCz13, 13, 0)
        ukladT.addWidget(naCz14, 14, 0)
        ukladT.addWidget(naCz15, 15, 0)
        ukladT.addWidget(naCz16, 16, 0)
        ukladT.addWidget(self.warCz1, 1, 1)
        ukladT.addWidget(self.warCz2, 2, 1)
        ukladT.addWidget(self.warCz3, 3, 1)
        ukladT.addWidget(self.warCz4, 4, 1)
        ukladT.addWidget(self.warCz5, 5, 1)
        ukladT.addWidget(self.warCz6, 6, 1)
        ukladT.addWidget(self.warCz7, 7, 1)
        ukladT.addWidget(self.warCz8, 8, 1)
        ukladT.addWidget(self.warCz9, 9, 1)
        ukladT.addWidget(self.warCz10, 10, 1)
        ukladT.addWidget(self.warCz11, 11, 1)
        ukladT.addWidget(self.warCz12, 12, 1)
        ukladT.addWidget(self.warCz13, 13, 1)
        ukladT.addWidget(self.warCz14, 14, 1)
        ukladT.addWidget(self.warCz15, 15, 1)
        ukladT.addWidget(self.warCz16, 16, 1)
        ukladT.addWidget(opis1, 1, 2)
        ukladT.addWidget(opis2, 2, 2)
        ukladT.addWidget(opis3, 3, 2)
        ukladT.addWidget(opis4, 4, 2)
        ukladT.addWidget(opis5, 5, 2)
        ukladT.addWidget(opis6, 6, 2)
        ukladT.addWidget(opis7, 7, 2)
        ukladT.addWidget(opis8, 8, 2)
        ukladT.addWidget(opis9, 9, 2)
        ukladT.addWidget(opis10, 10, 2)
        ukladT.addWidget(opis11, 11, 2)
        ukladT.addWidget(opis12, 12, 2)
        ukladT.addWidget(opis13, 13, 2)
        ukladT.addWidget(opis14, 14, 2)
        ukladT.addWidget(opis15, 15, 2)
        ukladT.addWidget(opis16, 16, 2)
        # 1-liniowe pola edycyjne WYNIKI
        ukladHH = QGridLayout()
        ukladHU = QGridLayout()
        self.wynikRF_P = QLineEdit()
        self.wynikRF_M = QLineEdit()
        self.uwagi = QLineEdit()
        self.wynikRF_P.readonly = True
        self.wynikRF_M.readonly = True
        self.wynikRF_P.setFixedWidth(60)
        self.wynikRF_M.setFixedWidth(60)
        self.wynikRF_P.setStyleSheet("background-color: #98D5FF")
        self.wynikRF_M.setStyleSheet("background-color: #98D5FF")
        wynik_RF_P = QLabel("CRF-p", self)
        wynik_RF_M = QLabel("CRF-m", self)
        wynik_RF_P.setFixedWidth(40)
        wynik_RF_M.setFixedWidth(40)
        opis_RF_P = QLabel("Wartość\tPredyspozycja\n0÷0,49\tNiska\t Strop wyrobiska jest stabilny.\n"
                           "0,5÷0,75\t Średnia \t Warunki panujące wokół wyrobiska predysponują występowanie opadów, "
                           "bądź obwałów \nskał. Zachodzi konieczność wykonania przebudowy wyrobiska na wysokości"
                           " pakietu kotwionych skał.\n0,76÷1\t Wysoka \t Warunki predysponują do wystąpienia  "
                           "przemieszczeń warstws tropowych powyżej \nkotwionego pakietu oraz wystąpienia zawału.", self)
        opis_RF_M = QLabel("Wartość\tZalecane działania\n"
                           "0÷0,59\tBrak konieczności podejmowania dodatkowych czynności.\n"
                           "0,6÷0,69\t Zwiększona częstotliwość kontroli i obserwacji wyrobiska np. odczyty z manometrów "
                           "stojaków \nhydraulicznych czy pomiary szerokości szczelin.\n"
                           "0,7÷0,9\t Zwiększony zakres badań np. endoskopem, dodatkowe otwory z pobraniem\n rdzeni "
                           "wiertniczych, obserwacje emisji akustycznej."
                           "0,91÷1\tObjęcie stałą sygnalizacją\n  i obserwacją stropów wyrobisk np. zabudowa elektronicznych "
                           "sygnalizatorów rozwarstwień czy stały\n nadzór podczas prac likwidacyjnych. Ograniczenie robót\n "
                           "wybierkowych w parcelach likwidacyjnych.", self)
        ukladHH.addWidget(wynik_RF_P, 20, 0)
        ukladHH.addWidget(wynik_RF_M, 21, 0)
        ukladHH.addWidget(opis_RF_P, 20, 2)
        ukladHH.addWidget(opis_RF_M, 21, 2)
        ukladHH.addWidget(self.wynikRF_P, 20, 1)
        ukladHH.addWidget(self.wynikRF_M, 21, 1)
        ukladHU.addWidget(self.uwagi, 22, 0)
        self.uwagi.setText(str("Uwagi:\t. Nazwa pola: RU-X/1.\tSkrzyżowanie: K-  /P-  ."))
        # buttons
        obliczBtn = QPushButton("Oblicz w&skaźniki", self)
        obliczBtn.resize(obliczBtn.sizeHint())
        ukladH = QHBoxLayout()
        ukladH.addWidget(obliczBtn)
        #
        ukladT.addLayout(ukladH, 18, 0, 1, 4)
        ukladT.addLayout(ukladHe,0, 0, 1, 4)
        ukladT.addLayout(ukladHH,20, 0, 1, 4)
        ukladT.addLayout(ukladHH,21, 0, 1, 4)
        ukladT.addLayout(ukladHU,22, 0, 1, 4)
        # przypisanie utworzonego układu do okna
        self.setLayout(ukladT)
        self.setGeometry(50, 80, 300, 300)
        self.setWindowIcon(QIcon('CRF.ico'))
        self.setWindowTitle("Prognoza zagrożenia zawałami - KGHM v.1.1")
        self.show()
        obliczBtn.clicked.connect(self.BUTTON_ACTION) #

    def BUTTON_ACTION(self):
        list_ = [self.warCz1.text(),self.warCz2.text(),self.warCz3.text(),self.warCz4.text(),self.warCz5.text(),self.warCz6.text(),self.warCz7.text(),self.warCz8.text(),
        self.warCz9.text(),self.warCz10.text(),self.warCz11.text(),self.warCz12.text(),self.warCz13.text(),self.warCz14.text(),self.warCz15.text(),self.warCz16.text()]
        
        try: list_ = [float(num.replace(",",".")) for num in list_]
        except: list_ = [x for x in list_ if x != '']
        
        print(list_, len(list_))
        try: loop(list_)
        #except: 
        except: 
            #self.Head.setText(str(sys.exc_info()[1]))
            self.set_output(
                str(sys.exc_info()[1]),
                str(sys.exc_info()[1])
                )

    def set_output(self, compute_pre, compute_mu):
        self.wynikRF_P.setText(str(compute_pre))
        self.wynikRF_M.setText(str(compute_mu))

def loop(date):
    compute_pre = "---"
    compute_mu = "---"

    try:
        if prepare.recon_length(date):
            date = prepare.clean_vector(date)
            compute_mu = neural_net._mu(
                date
                )
    except: pass
    
    if prepare.recon_length(date) or prepare.recon_length(date) == False:
        date = prepare.clean_vector(date, short= True)
        print('w pre', date)
        compute_pre = neural_net._pre(
            date  
        )

    state_msg = okno.uwagi.text() # user input # TO Z APP
    save = db.Save(state_msg, date)
    save.save_to_file(compute_mu,compute_pre)

    print(
        "PRE:", compute_pre,
        "\nMU:", compute_mu
    )
    #set_output(compute_mu)
    okno.set_output(compute_pre,compute_mu)

if __name__ == '__main__':
    import sys
    app_ = QApplication(sys.argv)
    okno = App_()
    sys.exit(app_.exec_())