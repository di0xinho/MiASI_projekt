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

from graphlayout import GraphLayout

functionScroll = None
"""functionScroll is list of user-defined functions"""

def setupTab2(parent):
    """
    Parameters:
    parent - Ui_Mainwindow class from ui_form.py
    """
    # create tab 2 widget
    parent.tab2 = QWidget()
    parent.tab2.setObjectName(u"tab2")
    parent.tabWidget.addTab(parent.tab2, "Wykresy (tab2)")
    parent.tab2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    parent.tab2Layout = QGridLayout()
    parent.tab2.setLayout(parent.tab2Layout)
    # nof columns and rows for tab2Layout. For now assume 8x6

    # function ScrollArea
    parent.functionScroll = QScrollArea(parent.tab2)
    parent.functionScroll.setObjectName(u"functionScroll")
    parent.functionScroll.setWidgetResizable(True) # ???
    parent.tab2Layout.addWidget(parent.functionScroll, 0, 0, 6, 3) # occupy whole column
    parent.functionScrollContent = QWidget()
    parent.functionScrollContent.setObjectName(u"functionScrollContents")
    parent.functionScroll.setWidget(parent.functionScrollContent)

    # Where function graphs will be displayed. This will be replaced by matplotlib widget.
    parent.graphWidget = QWidget(parent.tab2)
    parent.graphWidget.setObjectName(u"graphWidget")
    parent.tab2Layout.addWidget(parent.graphWidget, 0, 3, 4, 5)

    # keyboard grid widget 2. Special symbol keyboard
    parent.keyGridWidget2 = QWidget(parent.tab2)
    parent.keyGridWidget2.setObjectName(u"keyGridWidget2")
    parent.tab2Layout.addWidget(parent.keyGridWidget2, 4, 3, 2, 5)

    # keyboard grid 2
    parent.keyboardGrid2 = QGridLayout(parent.keyGridWidget2)
    parent.keyboardGrid2.setObjectName(u"keyboardGrid2")
    populateKeyboardGrid2(parent, parent.keyboardGrid2)
    pass

def populateKeyboardGrid2(parent, keyboardGrid2: QGridLayout):
    # random buttons
    # tworzenie przycisków "w pętli" wymaga makra / reflection czy podobnego mechanizmu. Może tablica/lista przycisków?
    # button 2.1
    parent.pushButton21 = QPushButton()
    parent.pushButton21.setObjectName(u"pushButton_5")
    keyboardGrid2.addWidget(parent.pushButton21, 0, 0, 1, 1)
    # button 2.2
    parent.pushButton22 = QPushButton()
    parent.pushButton22.setObjectName(u"pushButton_6")
    keyboardGrid2.addWidget(parent.pushButton22, 0, 1, 1, 1)
    # button 2.3
    parent.pushButton23 = QPushButton()
    parent.pushButton23.setObjectName(u"pushButton_7")
    keyboardGrid2.addWidget(parent.pushButton23, 1, 0, 1, 1)
    # button 2.4
    parent.pushButton24 = QPushButton()
    parent.pushButton24.setObjectName(u"pushButton_8")
    keyboardGrid2.addWidget(parent.pushButton24, 1, 1, 1, 1)
    pass