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

# TODO there's still a mess here, fix it
# TODO fix ui by adding h... or v... ...BoxLayouts

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
        #self.tabWidget.setContentsMargins(0,0,0,0)
        #self.tabWidget.setGeometry(QRect(90, 110, 551, 371)) # this works
        self.tabWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        MainWindow.setCentralWidget(self.tabWidget)


        # temporary
        # self.tab = QWidget()
        # self.tabWidget.addTab(self.tab, "TAB 1")
        # self.tab.setContentsMargins(0,0,0,0)
        # self.layoutToMakeTabsWork = QHBoxLayout()
        # self.tab.setLayout(self.layoutToMakeTabsWork) # there needs to be at least 1 layout in tabwidget's sub widgets
        # self.tab2 = QWidget()
        # self.tabWidget.addTab(self.tab2, "TAB 2")
        # self.lab1 = QLabel(self.tab)
        # self.lab1.setText("Elo, label 1")
        # self.tab1HLayout.addWidget(self.lab1)
        # self.lab2 = QLabel(self.tab2)
        # self.lab2.setText("Elo, label 2")

        self.setupTab1()
        self.setupTab2()

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

    def setupTab1(self):
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.tabWidget.addTab(self.tab1, "Naukowy (tab1)")
        self.tab1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.tab1Layout = QGridLayout()
        self.tab1.setLayout(self.tab1Layout)
        # TODO set nof columns and rows for tab1Layout. For now assume 8x6

        # Where formulas will be typed. This will be replaced by matplotlib widget.
        self.formulaWidget = QWidget()
        self.formulaWidget.setObjectName(u"widget")
        self.tab1Layout.addWidget(self.formulaWidget, 0, 0, 2, 5) # row, column, rowSpan, columnSpan. For some reason positional arguments don't work here

        # Where answer will be displayed. This will be replaced by matplotlib widget.
        self.answerWidget = QWidget()
        self.answerWidget.setObjectName(u"widget_2")
        self.tab1Layout.addWidget(self.answerWidget, 2, 0, 1, 5) # row, column, rowSpan, columnSpan.

        # keyboard grid widget 1. Special symbol keyboard
        self.keyGridWidget1 = QWidget()
        self.keyGridWidget1.setObjectName(u"gridLayoutWidget")
        self.tab1Layout.addWidget(self.keyGridWidget1, 3, 0, 3, 5) # row, column, rowSpan, columnSpan.

        # keyboard grid 1
        self.keyboardGrid1 = QGridLayout(self.keyGridWidget1)
        self.keyboardGrid1.setObjectName(u"gridLayout")
        self.populateKeyBoardGrid(self.keyboardGrid1)

        # history ScrollArea
        self.historyScroll = QScrollArea()
        self.historyScroll.setObjectName(u"historyScrollArea")
        self.historyScroll.setWidgetResizable(True) # ???
        self.tab1Layout.addWidget(self.historyScroll, 0, 5, 6, 3) # row, column, rowSpan, columnSpan. occupy whole column
        self.historyScrollContent = QWidget()
        self.historyScrollContent.setObjectName(u"scrollAreaWidgetContents")
        self.historyScroll.setWidget(self.historyScrollContent)
        pass

    def setupTab2(self):
        # create tab 2 widget
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.tabWidget.addTab(self.tab2, "Wykresy (tab2)")
        self.tab2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.tab2Layout = QGridLayout()
        self.tab2.setLayout(self.tab2Layout)
        # TODO set nof columns and rows for tab2Layout. For now assume 8x6

        # function ScrollArea
        self.functionScroll = QScrollArea(self.tab2)
        self.functionScroll.setObjectName(u"scrollArea_2")
        self.functionScroll.setWidgetResizable(True) # ???
        self.tab2Layout.addWidget(self.functionScroll, 0, 0, 6, 3) # occupy whole column
        self.functionScrollContent = QWidget()
        self.functionScrollContent.setObjectName(u"scrollAreaWidgetContents_2")
        self.functionScroll.setWidget(self.functionScrollContent)

        # Where function graphs will be displayed. This will be replaced by matplotlib widget.
        self.graphWidget = QWidget(self.tab2)
        self.graphWidget.setObjectName(u"widget_3")
        self.tab2Layout.addWidget(self.graphWidget, 0, 3, 4, 5)

        # keyboard grid widget 2. Special symbol keyboard
        self.keyGridWidget2 = QWidget(self.tab2)
        self.keyGridWidget2.setObjectName(u"gridLayoutWidget_2")
        self.tab2Layout.addWidget(self.keyGridWidget2, 4, 3, 2, 5)

        # keyboard grid 2
        self.keyboardGrid2 = QGridLayout(self.keyGridWidget2)
        self.keyboardGrid2.setObjectName(u"gridLayout_2")
        self.populateKeyboardGrid2(self.keyboardGrid2)

        pass

    def retranslateUi(self, MainWindow):
        #MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        # self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        # self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        # self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        # self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        # self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        # self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        # self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        # self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        pass
    # retranslateUi
