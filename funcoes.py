from itertools import count
from tkinter import W
import intel
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import threading
from time import sleep
import time
from custom_qstacked_widgets import *
import os
import ctypes


class funcoes():
    def changeimg(self):
        def theard():
            while True:
                try:
                    for i in range(4):
                        sleep(5)
                        self.images_games.setCurrentIndex(i)
                        if i == 0 :
                            self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">O Counter-Strike: Global Offensive (CS:GO) é a continuação do jogo de equipas cheio de ação que foi pioneiro quando </span></p><p><span style=\" color:#ffffff;\"> foi lançado há 12 anos atrás.</span></p></body></html>", None))
                        if i == 1:
                            self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">V\u00e1 para os c\u00e9us e experimente a alegria de voar na pr\u00f3xima gera\u00e7\u00e3o do Microsoft Flight Simulator.</span></p><p><span style=\" color:#ffffff;\"> </span></p><p><span style=\" color:#ffffff;\"> O mundo est\u00e1 ao seu alcance.</span></p></body></html>", None))
                        if i == 2:
                            self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">A história de Halo Infinite coloca Master Chief para enfrentar os conhecidos inimigos de outrora, como os Banidos.</span></p></body></html>", None))
                        if i == 3:
                            self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Forza Horizon 5 é um jogo eletrônico de corrida ambientado em um ambiente de mundo aberto sediado no México. </span></p><p><span style=\" color:#ffffff;\"> O jogo tem o maior mapa de toda a série Forza Horizon</span></p></body></html>", None))
                except:
                    pass
        thread = threading.Thread(target=theard)
        thread.start()  
        
    def progressbar(self):
        def therad():
            
            count = 0
            while count <= 200 :
                time.sleep(0.02)
                count = count +1
                self.progressBar.setValue(count)
                if count == 100:
                    self.stackedWidget.setCurrentIndex(1)
                    break
            #https://www.pythonguis.com/tutorials/multithreading-pyside-applications-qthreadpool/
        thread = threading.Thread(target=therad)
        thread.start()  
            
    def test_resol(self):
        if self.changeres.currentText() == '1366 x 768':
            w = 1366
            h  = 768
        if self.changeres.currentText() == '1920 x 1080':
            w = 1920
            h  = 1080
            
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        print(screensize)
        
        import win32api
        import win32con
        import pywintypes

        devmode = pywintypes.DEVMODEType()

        devmode.PelsWidth = w
        devmode.PelsHeight = h

        devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

        win32api.ChangeDisplaySettings(devmode, 0)