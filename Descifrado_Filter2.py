import sys
import math
import random
from PyQt4 import QtGui, QtCore

def create_matrix(n):
    matrix = [[0 for x in range(n)] for y in range(n)]
    return matrix

def rotate_matrix(matrix, dir):
    if dir == "clockwise":
        rotated = list(zip(*matrix[::-1]))
    elif dir == "counterclockwise":
        rotated = list(zip(*matrix))[::-1]
    return [list(i) for i in rotated]


def generate_key(key, n):
    real_key = create_matrix(n)
    max_index = int(n/2)
    counter = 1
    for i in range(0, 4):
        for x in range(0, max_index):
            for y in range(0, max_index):
                key[x][y] = counter
                counter += 1
        key = rotate_matrix(key, "counterclockwise")
        c_m = counter
        counter = 1
    rand_x = int(n / 2 * random.randint(0, 1))
    rand_y = int(n / 2 * random.randint(0, 1))
    for i in range(0, c_m):
        find_it = True
        for x in range(rand_x, n):
            for y in range(rand_y, n):
                if find_it and key[x][y] == i + 1:
                    real_key[x][y] = 1
                    find_it = False
        rand_x = int(n / 2 * random.randint(0, 1))
        rand_y = int(n / 2 * random.randint(0, 1))

    return real_key


def decrypt(c, k, dir):
    l = len(c)
    n = int(math.sqrt(l))
    crypt_c = create_matrix(n)
    counter = 0
    for x in range(n):
        for y in range(n):
            crypt_c[x][y] = c[counter]
            counter += 1
    key = k
    block = 0
    m = ''
    while block < 4:
        for x in range(0, n):
            for y in range(0, n):
                if key[x][y] == 1:
                    m += crypt_c[x][y]
                    crypt_c[x][y] = ' '
        key = rotate_matrix(key, dir)
        block += 1
    return m

def run(ciphertext,super_key):
    llave,direction,n,aux,j = super_key.split("/")
    n = int(n)
    key = create_matrix(n)
    j = int(j)
    counter = 0
    for x in range(n):
        for y in range(n):
            key[x][y] = int(aux[counter])
            counter += 1
    m = decrypt(ciphertext, key, direction)
    return m[:len(m)-j]



class window2(QtGui.QWidget):
    def __init__(self,text,key):
        super(window2, self).__init__()
        self._new_window = None
        self.initUI(text,key)
    def initUI(self,text,key):
        self.tx1 = QtGui.QLabel("TEXTO A DESCIFRAR",self)
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
        self.button2 = QtGui.QPushButton("DESCIFRAR", self)
        self.button2.clicked.connect(lambda: self.start(text,key))
        self.button2.move(460, 560)

        #------
        self.setGeometry(200, 100, 1000, 600)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('web.png'))
        self.setWindowTitle("Cifrado Filter 2")
        self.show()

    def start(self,text,key):
        self.textbox3.setText(run(str(text),str(key)))



if __name__ == '__main__':
    app = QtGui.QApplication([])
    gui = Window2()
    gui.show()
    app.exec_()
