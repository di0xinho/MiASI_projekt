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
    window_w = 800
    window_h = 600
    window_name = u"QT Calc 🐍" # u for unicode string

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

        ui_tab1.setupTab1(self)
        ui_tab2.setupTab2(self)

        # set starting tab
        self.tabWidget.setCurrentIndex(0)

        # translate
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    historyScroll = None
    """historyScroll is pist of previously calculated equations"""
    functionScroll = None
    """functionScroll is list of user-defined functions"""

    def populateKeyBoardGrid(self, keyboardGrid: QGridLayout):
        """Populate keyboard grid. First parameter is keyboardGrid reference. There are 3 ideas for second parameter:
            - pass tab number. 1 or 2
            - pass size keyboardGrid takes in its parent view
            - two different functions for two different tabs
            What about button names? Maybe pass also button list/tuple?
            """
        # some random buttons to populate keyboardGrid:
        # button 1.1
        self.pushButton11 = QPushButton()
        self.pushButton11.setObjectName(u"pushButton_1")
        keyboardGrid.addWidget(self.pushButton11, 0, 0, 1, 1)
        # button 1.2
        self.pushButton12 = QPushButton()
        self.pushButton12.setObjectName(u"pushButton_2")
        keyboardGrid.addWidget(self.pushButton12, 0, 1, 1, 1)
        # button 1.3
        self.pushButton13 = QPushButton()
        self.pushButton13.setObjectName(u"pushButton_3")
        keyboardGrid.addWidget(self.pushButton13, 1, 0, 1, 1)
        # button 1.4
        self.pushButton14 = QPushButton()
        self.pushButton14.setObjectName(u"pushButton_4")
        keyboardGrid.addWidget(self.pushButton14, 1, 1, 1, 1)
        pass

    def populateKeyboardGrid2(self, keyboardGrid2: QGridLayout):
        # random buttons
        # button 2.1
        self.pushButton21 = QPushButton()
        self.pushButton21.setObjectName(u"pushButton_5")
        keyboardGrid2.addWidget(self.pushButton21, 0, 0, 1, 1)
        # button 2.2
        self.pushButton22 = QPushButton()
        self.pushButton22.setObjectName(u"pushButton_6")
        keyboardGrid2.addWidget(self.pushButton22, 0, 1, 1, 1)
        # button 2.3
        self.pushButton23 = QPushButton()
        self.pushButton23.setObjectName(u"pushButton_7")
        keyboardGrid2.addWidget(self.pushButton23, 1, 0, 1, 1)
        # button 2.4
        self.pushButton24 = QPushButton()
        self.pushButton24.setObjectName(u"pushButton_8")
        keyboardGrid2.addWidget(self.pushButton24, 1, 1, 1, 1)
        pass

    def retranslateUi(self, MainWindow):
        #MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        pass
    # retranslateUi
