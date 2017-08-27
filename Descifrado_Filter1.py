import sys
from PyQt4 import QtGui, QtCore
from Descifrado_Filter2 import window2



def cesar(mensaje_cifrado,llave):
    mensaje=""
    for index,val in enumerate(mensaje_cifrado):
        caracter = ord(val) ^ ord(llave[0])
        car=caracter%253
        if car<32:
            car+=32
        mensaje += str(chr(car))
    return mensaje



class window(QtGui.QWidget):
    texto=""
    llave=""
    r=""
    def __init__(self):
        super(window, self).__init__()
        self._new_window = None
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
        self.button1 = QtGui.QPushButton("DESCIFRAR", self)
        self.button1.clicked.connect(lambda: self.start())
        self.button1.move(455, 290)
        self.textbox3 = QtGui.QTextEdit(self)
        self.textbox3.move(15,330)
        self.textbox3.resize(970, 220)
        self.textbox3.setReadOnly(True)
        self.button2 = QtGui.QPushButton("SIGUENTE", self)
        self.button2.clicked.connect(lambda: self.next())
        self.button2.move(460, 560)
        self.msgBox = QtGui.QMessageBox(self)
        self.msgBox.setText("Asegurate de completar los campos TEXTO A DESCIFRAR y LLAVE");
        self.msgBox2 = QtGui.QMessageBox(self)
        self.msgBox2.setText("Asegurate de dar click en el boton DESCIFRAR");
        #------
        self.setGeometry(200, 100, 1000, 600)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('web.png'))
        self.setWindowTitle("Descifrado Filter 1")
        self.show()
    def onChangedt1(self):
        self.texto=self.textbox.toPlainText()
    def onChangedt2(self):
        self.llave=self.textbox2.toPlainText()
    def start(self):
        if self.llave != "" and self.texto != "":
            self.textbox3.setText(cesar(str(self.texto),str(self.llave)))
        else:
            self.msgBox.exec_();
    def next(self):
        if self.textbox2.toPlainText() != "" :
            self._new_window = window2(str(self.textbox3.toPlainText()),str(self.llave))
            self._new_window.show()
            self.close()
        else:
            self.msgBox2.exec_();

if __name__ == '__main__':
    app = QtGui.QApplication([])
    gui = window()
    gui.show()
    app.exec_()
