# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'intelv1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from custom_qstacked_widgets import *

import sources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1547, 816)
        MainWindow.setStyleSheet(u"\n"
"border-radius:10px;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(0, 113, 197);\n"
"border:none;")
        self.stackedWidget.setFrameShape(QFrame.StyledPanel)
        self.stackedWidget.setFrameShadow(QFrame.Raised)
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.login.setStyleSheet(u"border-radius:10px;")
        self.verticalLayout_9 = QVBoxLayout(self.login)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_6 = QFrame(self.login)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 200))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.frame_6)

        self.frame_2 = QFrame(self.login)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_3)

        self.frame_logo = QFrame(self.frame_2)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setMaximumSize(QSize(354, 480))
        self.frame_logo.setStyleSheet(u"border-image:url(:/fundo/logo main.png);")
        self.frame_logo.setFrameShape(QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_logo)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_4)


        self.verticalLayout_9.addWidget(self.frame_2)

        self.frame = QFrame(self.login)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(600, 0))
        self.frame_7.setMaximumSize(QSize(16777215, 41))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.frame_7)

        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"border-radius:6px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.progressBar = QProgressBar(self.frame_9)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    text-align: center;\n"
"\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(85, 170, 255)\n"
"}\n"
"QProgressBar {\n"
"    min-height: 12px;\n"
"    max-height: 12px;\n"
"    border-radius: 6px;\n"
"}\n"
"QProgressBarr::chunk {\n"
"    border-radius: 6px;\n"
"    background-color: #009688;\n"
"}\n"
"QProgressBar {\n"
"    border: 2px solid #2196F3;\n"
"    border-radius: 5px;\n"
"    background-color: #E0E0E0;\n"
"}\n"
"#BlueProgressBar::chunk {\n"
"    background-color: #2196F3;\n"
"    width: 10px; \n"
"    margin: 0.5px;\n"
"}")
        self.progressBar.setValue(10)

        self.verticalLayout_10.addWidget(self.progressBar)


        self.horizontalLayout_9.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(600, 0))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.frame_10)


        self.verticalLayout_9.addWidget(self.frame)

        self.stackedWidget.addWidget(self.login)
        self.main = QWidget()
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"background-image: url(:/fundo/back2.jpg);\n"
"background-position: center;\n"
"background-repeat:no-repeat;\n"
"border: 0px;\n"
"")
        self.verticalLayout = QVBoxLayout(self.main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.uimain = QFrame(self.main)
        self.uimain.setObjectName(u"uimain")
        self.uimain.setMaximumSize(QSize(16777215, 16777215))
        self.uimain.setStyleSheet(u"")
        self.uimain.setFrameShape(QFrame.StyledPanel)
        self.uimain.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.uimain)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu = QFrame(self.uimain)
        self.menu.setObjectName(u"menu")
        self.menu.setMinimumSize(QSize(300, 0))
        self.menu.setMaximumSize(QSize(300, 16777215))
        self.menu.setStyleSheet(u"background-image: url();\n"
"background-color: rgba(0, 0, 10, 90);\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"\n"
"")
        self.menu.setFrameShape(QFrame.NoFrame)
        self.menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.mainlogo = QFrame(self.menu)
        self.mainlogo.setObjectName(u"mainlogo")
        self.mainlogo.setMinimumSize(QSize(0, 90))
        self.mainlogo.setMaximumSize(QSize(16777215, 90))
        self.mainlogo.setStyleSheet(u"background-color: rgba(0, 0, 0, 70);\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:0px;")
        self.mainlogo.setFrameShape(QFrame.StyledPanel)
        self.mainlogo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.mainlogo)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.mainlogo)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(100, 16777215))
        self.frame_8.setStyleSheet(u"background-image: url(:/fundo/60x60.png);\n"
"background-position: center;\n"
"background-repeat:no-repeat;\n"
"background-color: rgba(0, 0, 0, 0); \n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_8)

        self.label = QLabel(self.mainlogo)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"IntelOne Display")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgba(0, 0, 0, 0); \n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.mainlogo)

        self.categorias = QFrame(self.menu)
        self.categorias.setObjectName(u"categorias")
        self.categorias.setStyleSheet(u"background-color: rgba(0, 0, 0, 70);\n"
"border-top-left-radius:0px;\n"
"")
        self.categorias.setFrameShape(QFrame.StyledPanel)
        self.categorias.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.categorias)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrolbar = QFrame(self.categorias)
        self.scrolbar.setObjectName(u"scrolbar")
        self.scrolbar.setMinimumSize(QSize(0, 0))
        self.scrolbar.setMaximumSize(QSize(20, 16777215))
        self.scrolbar.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.scrolbar.setFrameShape(QFrame.StyledPanel)
        self.scrolbar.setFrameShadow(QFrame.Raised)
        self.animcurretnpage = QFrame(self.scrolbar)
        self.animcurretnpage.setObjectName(u"animcurretnpage")
        self.animcurretnpage.setGeometry(QRect(0, 75, 20, 5))
        self.animcurretnpage.setMinimumSize(QSize(20, 0))
        self.animcurretnpage.setMaximumSize(QSize(5, 10))
        self.animcurretnpage.setStyleSheet(u"background-color: rgb(0, 85, 255);")
        self.animcurretnpage.setFrameShape(QFrame.HLine)
        self.animcurretnpage.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.scrolbar)

        self.topmenu = QFrame(self.categorias)
        self.topmenu.setObjectName(u"topmenu")
        self.topmenu.setMinimumSize(QSize(0, 0))
        self.topmenu.setMaximumSize(QSize(250, 16777215))
        self.topmenu.setSizeIncrement(QSize(0, 20))
        self.topmenu.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.topmenu.setFrameShape(QFrame.StyledPanel)
        self.topmenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topmenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.topmenu)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(50, 0))
        self.pushButton_2.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamily(u"IntelOne Display")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_2.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_2.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"	border-radius:0px;\n"
"\n"
"	padding:15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")

        self.verticalLayout_8.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.topmenu)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(50, 0))
        self.pushButton_3.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamily(u"IntelOne Display")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"	border-radius:0px;\n"
"\n"
"	padding:15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")

        self.verticalLayout_8.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.topmenu)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(50, 0))
        self.pushButton_4.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_4.setFont(font2)
        self.pushButton_4.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"	border-radius:0px;\n"
"\n"
"	padding:15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")

        self.verticalLayout_8.addWidget(self.pushButton_4)

        self.pushButton_7 = QPushButton(self.topmenu)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(50, 0))
        self.pushButton_7.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_7.setFont(font2)
        self.pushButton_7.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"	border-radius:0px;\n"
"\n"
"	padding:15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")

        self.verticalLayout_8.addWidget(self.pushButton_7)

        self.pushButton_6 = QPushButton(self.topmenu)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(50, 0))
        self.pushButton_6.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_6.setFont(font2)
        self.pushButton_6.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"	border-radius:0px;\n"
"\n"
"	padding:15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")

        self.verticalLayout_8.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.topmenu)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font2)
        self.pushButton_5.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"	border-radius:0px;\n"
"\n"
"	padding:15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")

        self.verticalLayout_8.addWidget(self.pushButton_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.pushButton_8 = QPushButton(self.topmenu)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(50, 0))
        self.pushButton_8.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_8.setFont(font1)
        self.pushButton_8.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"	border-radius:0px;\n"
"\n"
"	padding:15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u":/fundo/notify.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QSize(24, 24))

        self.verticalLayout_8.addWidget(self.pushButton_8)


        self.horizontalLayout_5.addWidget(self.topmenu)


        self.verticalLayout_3.addWidget(self.categorias)


        self.horizontalLayout_3.addWidget(self.menu)

        self.content = QFrame(self.uimain)
        self.content.setObjectName(u"content")
        self.content.setMaximumSize(QSize(16777215, 16777215))
        self.content.setStyleSheet(u"background-image: url();\n"
"background-color: rgba(0, 0, 10, 200);\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.content)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toptools = QFrame(self.content)
        self.toptools.setObjectName(u"toptools")
        self.toptools.setMaximumSize(QSize(16777215, 35))
        self.toptools.setStyleSheet(u"background-image: url();\n"
"border:0px;\n"
"background-color: rgba(0, 0, 0,0);\n"
"")
        self.toptools.setFrameShape(QFrame.StyledPanel)
        self.toptools.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.toptools)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.minimize = QPushButton(self.toptools)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setMinimumSize(QSize(40, 40))
        self.minimize.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	background-image: url(:/fundo/minimize.png);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	background-image: url(:/fundo/minimize clik.png);\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.minimize)

        self.maxmize = QPushButton(self.toptools)
        self.maxmize.setObjectName(u"maxmize")
        self.maxmize.setMinimumSize(QSize(40, 40))
        self.maxmize.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	background-image: url(:/fundo/max 1.png);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	background-image: url(:/fundo/max_ click.png);\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.maxmize)

        self.exit = QPushButton(self.toptools)
        self.exit.setObjectName(u"exit")
        self.exit.setMinimumSize(QSize(40, 40))
        self.exit.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	background-image: url(:/fundo/close.png);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	background-image: url(:/fundo/close clik.png);\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.exit)


        self.verticalLayout_2.addWidget(self.toptools)

        self.contets = QStackedWidget(self.content)
        self.contets.setObjectName(u"contets")
        self.contets.setStyleSheet(u"background-image: url();\n"
"background-color: rgba(0, 0, 0,0);\n"
"")
        self.contets.setFrameShape(QFrame.StyledPanel)
        self.contets.setFrameShadow(QFrame.Raised)
        self.contetsPage1 = QWidget()
        self.contetsPage1.setObjectName(u"contetsPage1")
        self.verticalLayout_5 = QVBoxLayout(self.contetsPage1)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.PAG1 = QFrame(self.contetsPage1)
        self.PAG1.setObjectName(u"PAG1")
        self.PAG1.setStyleSheet(u"background-color: rgba(0, 0, 0,0);\n"
"")
        self.PAG1.setFrameShape(QFrame.StyledPanel)
        self.PAG1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.PAG1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(40, 0, 0, 0)
        self.TOPBUT = QFrame(self.PAG1)
        self.TOPBUT.setObjectName(u"TOPBUT")
        self.TOPBUT.setMaximumSize(QSize(16777215, 60))
        self.TOPBUT.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.TOPBUT.setFrameShape(QFrame.StyledPanel)
        self.TOPBUT.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.TOPBUT)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.TOPBUT)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(120, 40))
        font3 = QFont()
        font3.setFamily(u"IntelOne Display")
        font3.setPointSize(14)
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"	\n"
"border-bottom: 1px solid rgb(0, 188, 242);\n"
"	color: rgb(255, 255, 255);\n"
"    background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: center;\n"
"	border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 0); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"border-bottom: 1px solid rgb(0, 188, 242);\n"
"\n"
"}")

        self.horizontalLayout_7.addWidget(self.pushButton)

        self.pushButton_9 = QPushButton(self.TOPBUT)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(120, 40))
        self.pushButton_9.setFont(font3)
        self.pushButton_9.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"	\n"
"border-bottom: 3px solid rgba(255, 255, 255, 0); \n"
"	color: rgb(255, 255, 255);\n"
"    background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: center;\n"
"	border-radius:0px;border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 0); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"border-bottom: 1px solid rgb(0, 188, 242);\n"
"\n"
"}")

        self.horizontalLayout_7.addWidget(self.pushButton_9)

        self.horizontalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addWidget(self.TOPBUT)

        self.line = QFrame(self.PAG1)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.00214133 rgba(160, 160, 160, 255), stop:0.33833 rgba(54, 56, 121, 125), stop:0.66167 rgba(80, 58, 161, 27), stop:1 rgba(255, 255, 255, 192));")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.adss = QFrame(self.PAG1)
        self.adss.setObjectName(u"adss")
        self.adss.setMaximumSize(QSize(16777215, 16777215))
        self.adss.setStyleSheet(u"background-color: rgba(0, 0, 0, 0); ")
        self.adss.setFrameShape(QFrame.StyledPanel)
        self.adss.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.adss)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 50, 0)
        self.ads_esquerda = QFrame(self.adss)
        self.ads_esquerda.setObjectName(u"ads_esquerda")
        self.ads_esquerda.setMinimumSize(QSize(565, 34))
        self.ads_esquerda.setMaximumSize(QSize(16777215, 16777215))
        self.ads_esquerda.setStyleSheet(u"")
        self.ads_esquerda.setFrameShape(QFrame.StyledPanel)
        self.ads_esquerda.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.ads_esquerda)
        self.verticalLayout_7.setSpacing(30)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.boasvindas = QLabel(self.ads_esquerda)
        self.boasvindas.setObjectName(u"boasvindas")
        self.boasvindas.setMinimumSize(QSize(50, 0))
        self.boasvindas.setMaximumSize(QSize(16777215, 154))
        font4 = QFont()
        font4.setFamily(u"IntelOne Display")
        self.boasvindas.setFont(font4)

        self.verticalLayout_7.addWidget(self.boasvindas)

        self.line_2 = QFrame(self.ads_esquerda)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.00214133 rgba(160, 160, 160, 255), stop:0.33833 rgba(54, 56, 121, 125), stop:0.66167 rgba(80, 58, 161, 27), stop:1 rgba(255, 255, 255, 192));")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_2)

        self.funcao1 = QPushButton(self.ads_esquerda)
        self.funcao1.setObjectName(u"funcao1")
        self.funcao1.setMinimumSize(QSize(0, 120))
        self.funcao1.setMaximumSize(QSize(500, 16777215))
        font5 = QFont()
        font5.setFamily(u"IntelOne Display")
        font5.setPointSize(12)
        font5.setStyleStrategy(QFont.PreferAntialias)
        self.funcao1.setFont(font5)
        self.funcao1.setCursor(QCursor(Qt.PointingHandCursor))
        self.funcao1.setLayoutDirection(Qt.LeftToRight)
        self.funcao1.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"padding:15px;\n"
"\n"
"\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 75); \n"
"	 text-align: left;\n"
"border-radius:6px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"\n"
"border: 1px solid rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"\n"
"background-color: rgba(0, 0, 0, 0); \n"
"\n"
"}")
        self.funcao1.setAutoExclusive(False)

        self.verticalLayout_7.addWidget(self.funcao1)

        self.funcao2 = QPushButton(self.ads_esquerda)
        self.funcao2.setObjectName(u"funcao2")
        self.funcao2.setMinimumSize(QSize(0, 120))
        self.funcao2.setMaximumSize(QSize(500, 16777215))
        font6 = QFont()
        font6.setFamily(u"IntelOne Display")
        font6.setPointSize(12)
        self.funcao2.setFont(font6)
        self.funcao2.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"padding:15px;\n"
"\n"
"\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 75); \n"
"	 text-align: left;\n"
"border-radius:6px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"\n"
"border: 1px solid rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"\n"
"background-color: rgba(0, 0, 0, 0); \n"
"\n"
"}")

        self.verticalLayout_7.addWidget(self.funcao2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)


        self.horizontalLayout_6.addWidget(self.ads_esquerda)

        self.ads_direita = QFrame(self.adss)
        self.ads_direita.setObjectName(u"ads_direita")
        self.ads_direita.setMinimumSize(QSize(590, 1))
        self.ads_direita.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.ads_direita.setFrameShape(QFrame.StyledPanel)
        self.ads_direita.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.ads_direita)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(90, -1, 0, -1)
        self.verticalSpacer_5 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.images_games = QStackedWidget(self.ads_direita)
        self.images_games.setObjectName(u"images_games")
        self.images_games.setMinimumSize(QSize(500, 300))
        self.images_games.setMaximumSize(QSize(800, 600))
        self.images_games.setStyleSheet(u"background-position: center;\n"
"background-repeat:no-repeat;\n"
"background-color: rgba(0, 0, 0, 0); \n"
"border-radius: 7px;")
        self.images_games.setFrameShape(QFrame.StyledPanel)
        self.images_games.setFrameShadow(QFrame.Raised)
        self.img_gamepag1 = QWidget()
        self.img_gamepag1.setObjectName(u"img_gamepag1")
        self.img_gamepag1.setStyleSheet(u"border-image: url(:/ads-games/ads-games/csgo.jpg);\n"
"\n"
"")
        self.images_games.addWidget(self.img_gamepag1)
        self.img_gamepag2 = QWidget()
        self.img_gamepag2.setObjectName(u"img_gamepag2")
        self.img_gamepag2.setStyleSheet(u"border-image: url(:/ads-games/ads-games/msf.jpg);")
        self.images_games.addWidget(self.img_gamepag2)
        self.img_gamepag3 = QWidget()
        self.img_gamepag3.setObjectName(u"img_gamepag3")
        self.img_gamepag3.setStyleSheet(u"border-image: url(:/ads-games/ads-games/halo.jpg)")
        self.images_games.addWidget(self.img_gamepag3)
        self.img_gamepag4 = QWidget()
        self.img_gamepag4.setObjectName(u"img_gamepag4")
        self.img_gamepag4.setStyleSheet(u"border-image: url(:/ads-games/ads-games/forza5.jpg)")
        self.images_games.addWidget(self.img_gamepag4)

        self.verticalLayout_4.addWidget(self.images_games)

        self.label_3 = QLabel(self.ads_direita)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        self.label_3.setFont(font6)

        self.verticalLayout_4.addWidget(self.label_3)

        self.verticalSpacer_4 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.horizontalLayout_6.addWidget(self.ads_direita)


        self.verticalLayout_6.addWidget(self.adss)


        self.verticalLayout_5.addWidget(self.PAG1)

        self.contets.addWidget(self.contetsPage1)
        self.contetsPage2 = QWidget()
        self.contetsPage2.setObjectName(u"contetsPage2")
        self.TOPBUT_2 = QFrame(self.contetsPage2)
        self.TOPBUT_2.setObjectName(u"TOPBUT_2")
        self.TOPBUT_2.setGeometry(QRect(40, 0, 1205, 40))
        self.TOPBUT_2.setMaximumSize(QSize(16777215, 60))
        self.TOPBUT_2.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.TOPBUT_2.setFrameShape(QFrame.StyledPanel)
        self.TOPBUT_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.TOPBUT_2)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pushButton_10 = QPushButton(self.TOPBUT_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(120, 40))
        self.pushButton_10.setFont(font3)
        self.pushButton_10.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"	\n"
"border-bottom: 3px solid rgba(255, 255, 255, 0); \n"
"	color: rgb(255, 255, 255);\n"
"    background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 0); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"border-bottom: 1px solid rgb(0, 188, 242);\n"
"\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.TOPBUT_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(120, 40))
        self.pushButton_11.setFont(font3)
        self.pushButton_11.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"	\n"
"border-bottom: 1px solid rgb(0, 188, 242);\n"
"	color: rgb(255, 255, 255);\n"
"    background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: center;\n"
"	border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 0); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"border-bottom: 1px solid rgb(0, 188, 242);\n"
"\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_11)

        self.horizontalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)

        self.contets.addWidget(self.contetsPage2)

        self.verticalLayout_2.addWidget(self.contets)


        self.horizontalLayout_3.addWidget(self.content)


        self.verticalLayout.addWidget(self.uimain)

        self.stackedWidget.addWidget(self.main)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.contets.setCurrentIndex(0)
        self.images_games.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Centro de comando de\n"
"Gr\u00e1ficos Intel \u00ae", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Pagina Inicial", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Tela", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Sistema", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Suporte", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Preferencias", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Atualiza\u00e7\u00f5es", None))
        self.minimize.setText("")
        self.maxmize.setText("")
        self.exit.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Jogos", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Capturar", None))
        self.boasvindas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">A experi\u00eancia Perfeita espera por voc\u00ea </span></p><p><span style=\" font-size:13pt; color:#ffffff;\">Vincule todos os seus jogos em algumas etapas r\u00e1pidas para desbloquear</span></p><p><span style=\" font-size:13pt; color:#ffffff;\">op\u00e7\u00f5es de otimiza\u00e7\u00e3o eficientes para seus jogos</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.funcao1.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.funcao1.setText(QCoreApplication.translate("MainWindow", u"Detec\u00e7\u00e3o autom\u00e1tica\n"
"\n"
"Analisaremos todos os jogos compatives e permitiremos\n"
"que voce selecione quais deseja adicionar.", None))
        self.funcao2.setText(QCoreApplication.translate("MainWindow", u"Selecionar manualmente\n"
"Selecione um jogo para adicionar \u00e0 sua biblioteca.\n"
"", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">V\u00e1 para os c\u00e9us e experimente a alegria de voar na pr\u00f3xima gera\u00e7\u00e3o do Microsoft Flight Simulator.</span></p><p><span style=\" color:#ffffff;\"> O mundo est\u00e1 ao seu alcance.</span></p></body></html>", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Jogos", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Capturar", None))
    # retranslateUi

