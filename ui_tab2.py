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
    QTabWidget, QWidget, QListWidget, QListWidgetItem,
    QLabel, QHBoxLayout, QVBoxLayout)

from graphlayout import GraphLayout
import listelement
import helpbuttons as helpBT

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
    parent.tabWidget.addTab(parent.tab2, "Wykresy")
    parent.tab2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    parent.tab2Layout = QGridLayout()
    parent.tab2.setLayout(parent.tab2Layout)
    # nof columns and rows for tab2Layout. For now assume 8x6

    # function list
    parent.funcList = listelement.GraphList(parent.tab2) # not ui element
    parent.funcList.prepareFuncExample()
    parent.functionScroll = parent.funcList.list_widget
    parent.functionScroll.setObjectName(u"functionScroll")
    parent.tab2Layout.addWidget(parent.functionScroll, 0, 0, 6, 3) # occupy whole column

    # Where function graphs will be displayed
    parent.graphWidget = QWidget(parent.tab2)
    parent.graphWidget.setObjectName(u"graphWidget")
    parent.tab2Layout.addWidget(parent.graphWidget, 0, 3, 4, 5)
    # GraphLayout showing function 📈
    parent.graphDisplay = GraphLayout(True, True)
    parent.graphDisplay.plotExample()
    parent.graphWidget.setLayout(parent.graphDisplay.getLayout())

    # keyboard grid widget 2. Special symbol keyboard
    parent.keyGridWidget2 = QWidget(parent.tab2)
    parent.keyGridWidget2.setObjectName(u"keyGridWidget2")
    parent.tab2Layout.addWidget(parent.keyGridWidget2, 4, 3, 2, 5)

    # keyboard grid 2
    parent.keyboardGrid2 = QGridLayout(parent.keyGridWidget2)
    parent.keyboardGrid2.setObjectName(u"keyboardGrid2")
    populateKeyboardGrid2(parent)
    pass

def populateKeyboardGrid2(parent):
    "Populate keyboard grid in tab 2."
    
    # Here, keyboard will be a little different.
    # TODO modify keyboard to match function creation. x, y are certainly needed
    functionKeyboard = [
        'Ułamek', '.', '(', ')', 
        'sin', 'cos', 'tan', 'π',
        'Potęga', '√', 'log', 'e',
        'mod', 'abs'
    ] + helpBT.inserter(
        [f'{x}' for x in range(10)], # lista cyfr
        [(1, '/'), (4+1, '*'), (7+2, '+'), (10+3, '-')] # te liczby: przed jaką cyfrą wstawić element, to po +: ile już wstawiono. 10 nie ma, ale chodzi o to, że za 9
    )

    keyboardMaker = helpBT.KeboardHelp(parent.keyboardGrid2, parent.tab2Buttons)
    keyboardMaker.addButtons(functionKeyboard, 4)

    # Note: buttons can take more than one grid cell: keyboardGrid2.addWidget(parent.pushButton21, 0, 0, 2, 2)
    pass