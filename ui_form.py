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
    QTabWidget, QWidget)

# TODO there's still a mess here, fix it
# TODO fix ui by adding h... or v... ...BoxLayouts

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)

        # main, central widget
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # tab widget
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")

        # set central widget
        MainWindow.setCentralWidget(self.centralwidget)

        # menu bar
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        MainWindow.setMenuBar(self.menubar)

        # status bar
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # translate
        self.retranslateUi(MainWindow)

        # set starting tab
        self.tabWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def setupTab1(self):
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")

        # scroll area ?
        self.scrollArea = QScrollArea(self.tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True) # DELETE?
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # widget ?
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")

        # widget 2 ?
        self.widget_2 = QWidget(self.tab)
        self.widget_2.setObjectName(u"widget_2")

        # grid layout widget ?
        self.gridLayoutWidget = QWidget(self.tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")

        # grid layout
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")

        # button 1.1
        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        # button 1.2
        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        # button 1.3
        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)

        # button 1.4
        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)

        # add tab 1 to tab widget
        self.tabWidget.addTab(self.tab, "")
        pass

    def setupTab2(self):
        # create tab 2 widget
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")

        # grid layout widget 2 ?
        self.gridLayoutWidget_2 = QWidget(self.tab_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")

        # grid layout 2 ?
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        
        # button 2.1
        self.pushButton_5 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_2.addWidget(self.pushButton_5, 0, 0, 1, 1)

        # button 2.2
        self.pushButton_6 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_2.addWidget(self.pushButton_6, 0, 1, 1, 1)

        # button 2.3
        self.pushButton_7 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_2.addWidget(self.pushButton_7, 1, 0, 1, 1)

        # button 2.4
        self.pushButton_8 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_2.addWidget(self.pushButton_8, 1, 1, 1, 1)

        # scroll area 2
        self.scrollArea_2 = QScrollArea(self.tab_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)

        # scroll area widget
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        # widget 3 ?
        self.widget_3 = QWidget(self.tab_2)
        self.widget_3.setObjectName(u"widget_3")

        # add tab 2 to tab widget
        self.tabWidget.addTab(self.tab_2, "")
        pass

    def retranslateUi(self, MainWindow):
        pass
        # MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        # self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        # self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        # self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        # self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        # self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        # self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        # self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        # self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi
