from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import threading
from time import sleep
from intel import *
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from custom_qstacked_widgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from custom_qstacked_widgets import *

TIMER_SETA = 50

class efeitos():
    
    #effects.efeitos.shadow_widgets_ads_esquerda(self)
    def shadow_widgets_ads_esquerda(self):
                #SHADOW
        
        # efeito de somhbra
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 150))
        # frames aplicados:
        self.ads_esquerda.setGraphicsEffect(self.shadow)
        
    #effects.efeitos.shadow_widgets_ads_direita(self)
    def shadow_widgets_ads_direita(self):
                #SHADOW
        
        # efeito de somhbra
        self.shadow2 = QGraphicsDropShadowEffect(self)
        self.shadow2.setBlurRadius(20)
        self.shadow2.setXOffset(0)
        self.shadow2.setYOffset(0)
        self.shadow2.setColor(QColor(0, 92, 157, 150))
        # frames aplicados:
        self.menu.setGraphicsEffect(self.shadow2)
        
      #effects.efeitos.setamenu(self)

    def effectslide(self): #TODO TRANSICAO PRINCIPAL MAIN NAO MEXER
        self.contets.setTransitionDirection(QtCore.Qt.Horizontal)
        self.contets.setTransitionSpeed(100)
        self.contets.setTransitionEasingCurve(QtCore.QEasingCurve.Linear)
        self.contets.setSlideTransition(True)
    
    def transisaopage(self):
        duracao = 350
        print(self.animcurretnpage.geometry())
        off = self.animcurretnpage.geometry()
        self.animAE = QPropertyAnimation(self.ads_esquerda, b"geometry")
        self.animAE.setDuration(duracao)
        self.animAE.setStartValue(QRect(90, 0, 565, 740))
        self.animAE.setEndValue(QRect(0, 0, 565 , 740))
        self.animAE.start()
      
    
  

class setanimcurrent():
    global TIMER_SETA
    duracao = TIMER_SETA
    
    
    def anim1(self):
      global TIMER_SETA
      duracao = TIMER_SETA
      self.animA = QPropertyAnimation(self.animcurretnpage, b"geometry")
      self.animA.setDuration(duracao)
      self.animA.setStartValue(QRect(self.animcurretnpage.geometry()))
      self.animA.setEndValue(QRect(0, 24, 20, 5))
      self.animA.start()


      
    def anim2(self):
      global TIMER_SETA
      duracao = TIMER_SETA
      self.animb = QPropertyAnimation(self.animcurretnpage, b"geometry")
      self.animb.setDuration(duracao)
      self.animb.setStartValue(QRect(self.animcurretnpage.geometry()))
      self.animb.setEndValue(QRect(0, 75, 20, 5))
      self.animb.start()


    def anim3(self):
      global TIMER_SETA
      duracao = TIMER_SETA
      self.animc = QPropertyAnimation(self.animcurretnpage, b"geometry")
      self.animc.setDuration(duracao)
      self.animc.setStartValue(QRect(self.animcurretnpage.geometry()))
      self.animc.setEndValue(QRect(0, 126, 20, 5))
      self.animc.start()


      
    def anim4(self):
      global TIMER_SETA
      duracao = TIMER_SETA
      self.animd = QPropertyAnimation(self.animcurretnpage, b"geometry")
      self.animd.setDuration(duracao)
      self.animd.setStartValue(QRect(self.animcurretnpage.geometry()))
      self.animd.setEndValue(QRect(0, 177, 20, 5))
      self.animd.start()


    def anim5(self):
      global TIMER_SETA
      duracao = TIMER_SETA
      self.anime = QPropertyAnimation(self.animcurretnpage, b"geometry")
      self.anime.setDuration(duracao)
      self.anime.setStartValue(QRect(self.animcurretnpage.geometry()))
      self.anime.setEndValue(QRect(0, 228, 20, 5))
      self.anime.start()


    def anim6(self):
      global TIMER_SETA
      duracao = TIMER_SETA
      self.animf = QPropertyAnimation(self.animcurretnpage, b"geometry")
      self.animf.setDuration(duracao)
      self.animf.setStartValue(QRect(self.animcurretnpage.geometry()))
      self.animf.setEndValue(QRect(0, 279, 20, 5))
      self.animf.start()


