import sys
from PyQt4 import QtGui, QtCore


class window2(QtGui.QWidget):
    def __init__(self,text,key):
        super(window2, self).__init__()
        self._new_window = None
        self.initUI(text,key)
    def initUI(self,text,key):

        self.tx1 = QtGui.QLabel("TEXTO A CIFRAR",self)
        self.tx1.move(200, 0)
        self.tx2 = QtGui.QLabel("LLAVE",self)
        self.tx2.move(730, 0)
        self.textbox = QtGui.QTextEdit(self)
        self.textbox.move(15, 30)
        self.textbox.resize(475, 250)
        self.textbox.setText(text)
        self.textbox2 = QtGui.QTextEdit(self)
        self.textbox2.move(515, 30)
        self.textbox2.resize(470, 250)
        self.textbox2.setText(key)
        self.textbox3 = QtGui.QTextEdit(self)
        self.textbox3.move(15,330)
        self.textbox3.resize(970, 220)
        self.textbox3.setReadOnly(True)
        self.textbox2.setReadOnly(True)
        self.textbox.setReadOnly(True)
        self.button2 = QtGui.QPushButton("CIFRAR", self)
        self.button2.clicked.connect(lambda: self.start(text,key))
        self.button2.move(460, 560)

        #------
        self.setGeometry(200, 100, 1000, 600)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('web.png'))
        self.setWindowTitle("Cifrado Filter 2")
        self.show()

    def start(self,text,key):
        self.textbox3.setText(cesar(str(text),str(key)))



if __name__ == '__main__':
    app = QtGui.QApplication([])
    gui = Window2()
    gui.show()
    app.exec_()



def cesar(mensaje,llave):
    mensaje_cifrado=""
    for index,val in enumerate(mensaje):
        caracter = ord(val) ^ ord(llave[0])
        car=caracter%253
        if car<32:
            car+=32
        mensaje_cifrado += str(chr(car))
    return mensaje_cifrado
