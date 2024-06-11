# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
## Created by: Qt User Interface Compiler version 6.6.0
################################################################################

from constants import MAINFILE
if __name__ == "__main__":
    print(f"\nTo start calculator run {MAINFILE} file.\n")
    exit(0)

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QStatusBar,
    QTabWidget, QWidget,
    QLabel, QHBoxLayout, QVBoxLayout)

from GraphLayout import GraphLayout

import ui_tab2
import ui_tab1

class Ui_MainWindow(object):
    window_w = 1200
    window_h = 800
    window_name = u"QT Calc 🐍" # u for unicode string
    def __init__(self) -> None:
        super().__init__()
        self.tab1Buttons = {}
        self.tab2Buttons = {}
        pass

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(self.window_w, self.window_h)
        MainWindow.setWindowTitle(self.window_name)

        # main, central widget
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        #MainWindow.setCentralWidget(self.centralwidget)
        self.centralwidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.centralwidget.setContentsMargins(0,0,0,0)

        # menu bar
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        MainWindow.setMenuBar(self.menubar)

        # status bar
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)


        # tab widget
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        MainWindow.setCentralWidget(self.tabWidget)

        ui_tab1.setupTab1(self, self.window_h)
        ui_tab2.setupTab2(self)

        # set starting tab
        self.tabWidget.setCurrentIndex(0)

        # translate
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        #MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        pass
    # retranslateUi
