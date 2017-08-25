import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    texto=""
    llave=""
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.tx1 = QtGui.QLabel("TEXTO A DESCIFRAR",self)
        self.tx1.move(200, 0)
        self.tx2 = QtGui.QLabel("LLAVE",self)
        self.tx2.move(730, 0)
        self.textbox = QtGui.QTextEdit(self)
        self.textbox.move(15, 30)
        self.textbox.resize(475, 250)
        self.textbox.textChanged.connect(self.onChangedt1)
        self.textbox2 = QtGui.QTextEdit(self)
        self.textbox2.move(515, 30)
        self.textbox2.resize(470, 250)
        self.textbox2.textChanged.connect(self.onChangedt2)
        self.button1 = QtGui.QPushButton("DESENCRIPTAR", self)
        self.button1.clicked.connect(lambda: self.start(self.texto,self.llave))
        self.button1.move(455, 290)
        self.textbox3 = QtGui.QTextEdit(self)
        self.textbox3.move(15,330)
        self.textbox3.resize(970, 220)
        self.textbox3.setReadOnly(True)
        self.button2 = QtGui.QPushButton("SIGUENTE", self)
        self.button2.clicked.connect(lambda: self.start())
        self.button2.move(460, 560)

        #------
        self.setGeometry(200, 100, 1000, 600)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('web.png'))
        self.setWindowTitle("HILL")
        self.show()
    def onChangedt1(self):
        self.texto=self.textbox.toPlainText()
    def onChangedt2(self):
        self.llave=self.textbox2.toPlainText()
    def start(self,texto,llave):
        self.textbox3.setText(cesar(str(self.texto),str(self.llave)))



def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

def cesar(mensaje_cifrado,llave):
    mensaje=""
    for index,val in enumerate(mensaje_cifrado):
        caracter = ord(val) ^ ord(llave[0])
        mensaje += str(chr(caracter))
    return mensaje

if __name__ == '__main__':
    main()
