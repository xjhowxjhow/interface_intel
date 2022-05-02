import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from intel import Ui_MainWindow
import funcoes
import effects
from custom_qstacked_widgets import *

WINDOW_SIZE = 0;

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setupUi(self)
        self.showFullScreen() 
        loadJsonStyle(self)
        
        #BARRA DE PROGRESSO
        funcoes.funcoes.progressbar(self)
        
        #FUNCOES
        funcoes.funcoes.changeimg(self)
                
        #JANELA FUNCOES
        self.minimize.clicked.connect(lambda: self.showMinimized())
        self.exit.clicked.connect(lambda: self.close())
        self.maxmize.clicked.connect(lambda: self.restore_or_maximize_window())
        
        #SOMBRAS E EFEITOS
        effects.efeitos.shadow_widgets_ads_direita(self)
        effects.efeitos.shadow_widgets_ads_esquerda(self)
        effects.efeitos.effectslide(self)

        #BOTOES AÇÃO EFEITOS     
        self.pushButton_2.clicked.connect(lambda:effects.setanimcurrent.anim1(self))
        self.pushButton_3.clicked.connect(lambda:effects.setanimcurrent.anim2(self))
        self.pushButton_4.clicked.connect(lambda:effects.setanimcurrent.anim3(self))
        self.pushButton_7.clicked.connect(lambda:effects.setanimcurrent.anim4(self))
        self.pushButton_6.clicked.connect(lambda:effects.setanimcurrent.anim5(self))
        self.pushButton_5.clicked.connect(lambda:effects.setanimcurrent.anim6(self))        
        self.pushButton.clicked.connect(lambda:effects.efeitos.transisaopage(self))
        self.pushButton_10.clicked.connect(lambda:effects.efeitos.transisaopage(self))
        
        #BOTOES AÇÃO FUNCOES
        self.pushButton_3.clicked.connect(lambda:self.contets.setCurrentIndex(1))
        self.pushButton_2.clicked.connect(lambda:self.contets.setCurrentIndex(0))

    def restore_or_maximize_window(self):
        # variavel global windows tela janela
        global WINDOW_SIZE
        win_status = WINDOW_SIZE
        if win_status == 0:
            WINDOW_SIZE = 1 
            self.showFullScreen() 
        else:
            WINDOW_SIZE = 0 
            self.showNormal()
    #MOVE JANELA
    def mousePressEvent(self, event):
        self.offset = event.pos()   
    #MOVE JANELA
    def mouseMoveEvent(self, event):
        x=event.globalX()
        y=event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x-x_w, y-y_w)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit()
