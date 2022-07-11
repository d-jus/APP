from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout
from PyQt5 import QtCore
from numpy import exp, array, delete, swapaxes, add, matmul
from tkinter import messagebox as msb




#msb.showinfo(title="Informacja od autorów", message="Używasz programu typu MVP (ang. minimum viable product), wersji z podstawową funkcjonalnością w celu przygotowania informacji zwrotnej dla dalszego rozwoju produktu. ")

class Kalkulator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        #self.setStyleSheet("background-color: #FCF3E8")
        self.interfejs()


    ### SILNIK SSN ###
    def SSN(self, vectorIN):

        def normalization_input(n1, n2, n3, n4):
            return (n1 - n2) * n3 + n4

        def sigmoid(net):
            return 2 / (1 + exp(-2 * net)) - 1

        if len(vectorIN) == 16:
            input_vectorP = array(vectorIN)
            input_vectorP = delete(input_vectorP,[10, 11, 12, 13])  # usuwanie elementów z cztnników techniczne: 11,12,13 i nr 14
        if len(vectorIN) == 12:
            input_vectorP = array(vectorIN)

        # dla wskaźnika predyspozycja
        b = array([-0.287687978354995, -0.254145744490595, 0.20553506200414, -2.64574989693001])
        b2 = array([0.6846354027686])
        input_weight = array([
            [1.26725653798838, 1.65759921776273, -5.0361717639055, 1.76956731042433, -0.431163288154406, 3.69734722319648,
             1.02857507722956, 0.661808275883479, 0.209339900564082, -1.01218853442114, -1.46969028554141,
             0.541256438501523],
            [-3.09292725249879, -0.103860099051127, 1.72955873331385, -1.87811515801954, -1.33087890523572,
             -1.55636303276972, 1.48442141789297, 1.09271101838906, 3.11750816221168, -0.27260972401501, -2.45435091937436,
             0.674],
            [0.378954618515674, -1.52815854327969, 2.01602090239542, 0.542536531440565, -0.450314982981614,
             -0.700092491637342, -1.08494621589648, 2.07711316155165, 0.507439221130574, 0.632858935601814, 2.6056773976665,
             0.018411737451537],
            [-1.46464314259969, -1.25355425619272, 0.121131988360189, 0.119618446510931, -0.268135668843527,
             -0.74153680952656, 4.26132597267561, -2.77097846630327, 1.16962178643047, 3.20457679748779, 0.419723937623802,
             0.14]
        ])
        layer_weight = array([
            [0.346098756218088, 0.250774431519168, 0.508091158190255, -0.729919889465312]
        ])

        #input_vector = np.array([5, 11.8, 0, 0.3, 0, 0, 18, 18, 0, 1.1, 0, 0])
        #input_vector = np.array([5, 11.8, 0, 0.3, 0, 0, 18, 18, 0, 1.1, 0, 0])
        a1 = array([2, 5.4, 0, 0, 0, 0, 0, 0, 0, 0.6, 0, 0])
        a2 = array(
            [0.037037037037037, 0.3125, 2, 2, 4, 2, 0.0666666666666667, 0.04, 0.0105263157894737, 3.47826086956522, 2,
             0.434782608695652])
        a3 = array([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])

        normalization_inpuT = normalization_input(input_vectorP, a1, a2, a3)

        input_weight = swapaxes(input_weight, 0, 1)
        layer_weight = swapaxes(layer_weight, 0, 1)
        net = add(matmul(normalization_inpuT, input_weight), b)
        a_1 = sigmoid(net)
        a_2_pre = add(matmul(a_1, layer_weight), b2)
        normalization_output_pre = (a_2_pre + 1) / 3.33333333333333 + 0.4
        self.wynikRF_P.setText(str(round(normalization_output_pre[0], 4)))
        self.wynikRF_M.setText(str("--"))
        # dla wskaźnika możliwość utrzymania
        if len(vectorIN) == 16:
            b = array([1.48339316887219, 1.08492883208489, -0.793974006244905, 0.728464525709856, -0.564220413029404,
                          -0.271066479479504, 2.03566940410352, 2.20051665768103])
            b2 = array([0.565940872595944])
            input_weight = array([
                [-0.380243288993, -0.300175201712818, -0.281004440161411, -0.332830486360074, 0.156008642457155,
                 0.111678603030612, -0.683603556539849, -0.642223750037346, 1.15597327801351, 0.609205864624937,
                 -0.702303822551299, 0.0406362614401268, 0.401893364670345, -0.827294642045006, 0.0949570653356762,
                 0.524829622005859],
                [-1.08533173309714, -0.21256961759385, 0.0742364961730546, 0.399930564553522, -0.262091017398624,
                 -0.603223339698924, -0.169185278065604, 0.127448582732462, 0.0132862240972325, -0.198066501449639,
                 0.184217193385349, -0.314833238487254, -0.118995209333859, -0.777992847269311, 0.59367024069462,
                 -0.651660258008262],
                [0.225954459695221, -0.904010911207907, 0.435670015063225, -0.0578680209135651, -0.346748531086589,
                 1.12107741090145, -0.933281918488416, -0.89862634991907, -0.573580415623607, -0.608260540893736,
                 0.256716361311498, 1.04636200791995, -0.559515343333687, -0.0911404609438948, 0.0651366891541776,
                 0.263701219294465],
                [0.0194896271876738, 0.433047881018382, -0.420428771632105, 1.00366562908406, 0.355891858986215,
                 0.0729908336797084, 0.18868121433102, -0.0107430299531131, 1.12928089337506, 0.233822185502071,
                 0.553956900836664, 0.537905688270666, -0.585058638822749, 0.489283687789724, 0.343112638867919,
                 -0.266998526994917],
                [0.0752769450394558, 0.12075061401691, -0.186714651102901, -0.391503689471921, -0.122217954984165,
                 0.907059939667972, 1.08151651219626, -0.912485238218247, -0.102591181086309, -0.210618125712561,
                 0.329981305884741, -0.784274645667204, -0.62533927148021, 0.814162895812021, -1.29585754439226,
                 -0.767895670839157],
                [-1.42876798833839, 0.788096832811516, 0.76056473348001, -0.723287125347485, -0.00752786112364666,
                 -0.0747843845283547, 0.354566122916609, 0.537957232800058, -0.0233729787134534, -0.572433630067002,
                 -0.511804811414359, 0.0730100779106406, 0.0943613910592733, -0.469325473925219, -0.478139056321774,
                 -0.0808742129487763],
                [0.552317263450101, -0.532374967991816, 0.731469518361806, -0.94714303798499, -0.149561811304513,
                 0.297131656767043, -0.378634753131337, 0.516353506485357, 0.718832704565303, -1.40522662615197,
                 -0.1783914723723, -0.13067869858491, -0.998410170798229, -0.346063328263863, -1.62149816939453,
                 0.0356453338492707],
                [-0.346664681172561, -0.207508342892562, 0.135215865753101, 0.418742306490479, 0.323270397619853,
                 0.702086118402546, 1.04029549224016, 1.03398501629487, -0.967928603233751, 0.0294362921521164,
                 0.0174556715112133, 0.0262080756533385, -0.217919115720474, 0.369681669267974, 0.745135266386719,
                 -0.345331748196849]
            ])
            layer_weight = array([
                [-0.611677244453564, -0.255096748946293, 0.683630206037378, 0.287687247426353, -0.659235559810339,
                 0.046307415273694, 0.839652480771805, 0.468721325466003]
            ])

            input_vector = array(vectorIN)
            #input_vector = np.array([5, 11.8, 0, 0.3, 0, 0, 18, 18, 0, 1.1, 17.5, 1.8, 0, 3.5, 0, 0])
            a1 = array([2, 5.4, 0, 0, 0, 0, 0, 0, 0, 0.6, 6.4, 1.6, 0, 0.5, 0, 0])
            a2 = array(
                [0.037037037037037, 0.3125, 2, 2, 4, 2, 0.0666666666666667, 0.04, 0.0105263157894737, 3.47826086956522,
                 0.18018018018018, 2, 0.0444444444444444, 0.307692307692308, 2, 0.434782608695652])
            a3 = array([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])

            normalization_Input = normalization_input(input_vector, a1, a2, a3)

            input_weight = swapaxes(input_weight, 0, 1)
            layer_weight = swapaxes(layer_weight, 0, 1)

            net = add(matmul(normalization_Input, input_weight), b)

            a_1 = sigmoid(net)

            a_2 = add(matmul(a_1, layer_weight), b2)

            normalization_output = (a_2 + 1) / 2.85714285714286 + 0.3

        # print("Wartość wskaźnika możliwość utrzymania: {0}\nWartość wskaźnika predysozycja: {1}".format(
        #     round(normalization_output[0], 2), round(normalization_output_pre[0], 2)))
            self.wynikRF_M.setText(str(round(normalization_output[0], 2)))




    def interfejs(self):

        # etykiety
        head = "Metoda oceny zagrożenia obwałami i opadem skał stropowych\nopracowana dla warunków polskich kopalń rud miedzi\n"
        naHead = QLabel(head, self)
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



        naCz1 = QLabel(naCz1OP, self)
        naCz2 = QLabel(naCz2OP, self)
        naCz3 = QLabel(naCz3OP, self)
        naCz4 = QLabel(naCz4OP, self)
        naCz5 = QLabel(naCz5OP, self)
        naCz6 = QLabel(naCz6OP, self)
        naCz7 = QLabel(naCz7OP, self)
        naCz8 = QLabel(naCz8OP, self)
        naCz9 = QLabel(naCz9OP, self)
        naCz10 = QLabel(naCz10OP, self)
        naCz11 = QLabel(naCz11OP, self)
        naCz12 = QLabel(naCz12OP, self)
        naCz13 = QLabel(naCz13OP, self)
        naCz14 = QLabel(naCz14OP, self)
        naCz15 = QLabel(naCz15OP, self)
        naCz16 = QLabel(naCz16OP, self)

        opis1 = QLabel(opis1OP, self)
        opis2 = QLabel(opis2OP, self)
        opis3 = QLabel(opis3OP, self)
        opis4 = QLabel(opis4OP, self)
        opis5 = QLabel(opis5OP, self)
        opis6 = QLabel(opis6OP, self)
        opis7 = QLabel(opis7OP, self)
        opis8 = QLabel(opis8OP, self)
        opis9 = QLabel(opis9OP, self)
        opis10 = QLabel(opis10OP, self)
        opis11 = QLabel(opis11OP, self)
        opis12 = QLabel(opis12OP, self)
        opis13 = QLabel(opis13OP, self)
        opis14 = QLabel(opis14OP, self)
        opis15 = QLabel(opis15OP, self)
        opis16 = QLabel(opis16OP, self)

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

        #
        ukladT = QGridLayout()
        #
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

        # przyciski
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

        obliczBtn.clicked.connect(self.obliczenia)

    def obliczenia(self):
        try:
        # self.checkCoeIn()
            zmienne=[self.warCz1.text(),self.warCz2.text(),self.warCz3.text(),self.warCz4.text(),self.warCz5.text(),self.warCz6.text(),self.warCz7.text(),self.warCz8.text(),
                     self.warCz9.text(),self.warCz10.text(),self.warCz11.text(),self.warCz12.text(),self.warCz13.text(),self.warCz14.text(),self.warCz15.text(),self.warCz16.text()]
            wektor = []
            for i in zmienne:
                aA=float(i.replace(",","."))
                wektor.append(aA)
            print(wektor)
            self.SSN(wektor)                           # do silnika SSN
            ah = (wektor)
            uwagiZap = self.uwagi.text()
            ag = ("wartość czynników: {0} \t {1} \n".format(ah, uwagiZap))
            with open('SSN_prognozy.txt', 'a') as fd:
                fd.write(ag)
        except ValueError:
            print("Oops!  wyskoczył jakiś błąd\n nie obliczono wskaźnika MU")
            try:
                zmienne = [self.warCz1.text(), self.warCz2.text(), self.warCz3.text(), self.warCz4.text(),
                           self.warCz5.text(), self.warCz6.text(), self.warCz7.text(), self.warCz8.text(),
                           self.warCz9.text(), self.warCz10.text(), self.warCz15.text(), self.warCz16.text()]
                wektor = []
                for i in zmienne:
                    aA = float(i.replace(",", "."))
                    wektor.append(aA)
                print(wektor)
                self.SSN(wektor)  # do silnika SSN
                ah = (wektor)
                uwagiZap=self.uwagi.text()
                ag = ("wartość czynników (tylko predyspozycja): {0} \t {1} \n".format(ah, uwagiZap))
                with open('SSN_prognozy.txt', 'a') as fd:
                    fd.write(ag)
            except ValueError:
                print("Oops!  wyskoczył jakiś błąd\n nie obliczono nic")
                self.wynikRF_P.setText(str("- - -"))
                self.wynikRF_M.setText(str("- - -"))


if __name__ == '__main__':
    import sys


    app = QApplication(sys.argv)
    okno = Kalkulator()
    sys.exit(app.exec_())