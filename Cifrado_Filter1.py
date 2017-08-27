import sys
import math
import random
from PyQt4 import QtGui, QtCore
from Cifrado_Filter2 import window2

def create_matrix(n):
    matrix = [[0 for x in range(n)] for y in range(n)]
    return matrix


def print_key(direction, n, key, Ll):
    M = direction + "/" + str(n) + "/"
    for x in range(0, n):
        for y in range(0, n):
            M += str(key[x][y])
    M += "/" + Ll
    return M


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


def crypt(m, k, dir, n):
    crypt_m = create_matrix(n)
    key = k
    block_size = int(len(m)/4)
    block = 0
    i = 0
    while block < 4:
        for x in range(0, n):
            for y in range(0, n):
                if key[x][y] == 1:
                    crypt_m[x][y] = m[i]
                    i += 1
        key = rotate_matrix(key, dir)
        block += 1
    c = ""
    for x in range(0, n):
        for y in range(0, n):
            c += crypt_m[x][y]

    return c

def run(plaintext):
    ## Plaintext traitment
    l = len(plaintext)
    n = int(math.ceil(math.sqrt(l)))
    if n % 2 != 0:
        n += 1
    L = n ** 2
    if L > l:
        plaintext += "j" * (L - l)
    ## Creation of a valid key
    key_body = create_matrix(n)
    key = generate_key(key_body, n)
    ## Selection of a encrypt direction
    temp_dir = random.randint(0, 1)
    if temp_dir == 0:
        direction = "clockwise"
    else:
        direction = "counterclockwise"
    ## Encrypt!
    return [crypt(plaintext, key, direction, n),print_key(direction,n,key,str(L-l))]

class window(QtGui.QWidget):
    texto=""
    llave=""
    r=""
    def __init__(self):
        super(window, self).__init__()
        self._new_window = None
        self.initUI()

    def initUI(self):

        self.tx1 = QtGui.QLabel("TEXTO A CIFRAR",self)
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
        self.button1 = QtGui.QPushButton("CIFRAR", self)
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
        self.msgBox.setText("Asegurate de completar los campos TEXTO A CIFRAR y LLAVE");
        self.msgBox2 = QtGui.QMessageBox(self)
        self.msgBox2.setText("Asegurate de dar click en el boton CIFRAR");
        #------
        self.setGeometry(200, 100, 1000, 600)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('web.png'))
        self.setWindowTitle("Cifrado Filter 1")
        self.show()
    def onChangedt1(self):
        self.texto=self.textbox.toPlainText()
    def onChangedt2(self):
        self.llave=self.textbox2.toPlainText()
    def start(self):
        if self.llave != "" and self.texto != "":
            self.r = run(str(self.texto))
            self.llave=str(self.llave)+"/"+(str(self.r[1]))
            self.textbox2.setText(self.llave)
            self.textbox3.setText((str(self.r[0])))
        else:
            self.msgBox.exec_();
    def next(self):
        if self.textbox3.toPlainText() != "" :
            self._new_window = window2((str(self.r[0])),self.llave)
            self._new_window.show()
            self.close()
        else:
            self.msgBox2.exec_();

if __name__ == '__main__':
    app = QtGui.QApplication([])
    gui = window()
    gui.show()
    app.exec_()
