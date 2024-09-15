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
from helpers import onEqualClick, setupButtons, addToExpression, removeExpression, removeLastCharacter
import helpbuttons as helpBT
import listelement

# historyScroll and functionScroll will contain dynamically set Widgets with GraphLayout
historyScroll = None
"""historyScroll is list of previously calculated equations"""

def setupTab1(parent, totalHeight = 0):
    """
    Parameters:
    parent - Ui_Mainwindow class from ui_form.py
    totalHeight - if > 0: set constant height of elements.
    This solves bug with incorrect widget size proportions, but unfortunately means no responsive layout.
    """
    parent.tab1 = QWidget()
    parent.tab1.setObjectName(u"tab1")
    parent.tabWidget.addTab(parent.tab1, "Naukowy")
    parent.tab1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    parent.tab1Layout = QGridLayout()
    parent.tab1.setLayout(parent.tab1Layout)
    # nof rows and columns is 8x6

    # Widget to hold GraphLayout
    parent.formulaWidget = QWidget()
    parent.formulaWidget.setObjectName(u"formulaWidget")
    parent.formulaWidget.setStyleSheet("QWidget#formulaWidget { border: 1px solid black; }")
    parent.tab1Layout.addWidget(parent.formulaWidget, 0, 0, 2, 5) # row, column, rowSpan, columnSpan. For some reason positional arguments don't work here
    # GraphLayout for input
    parent.mathFormula = GraphLayout(True)
    parent.mathFormula.formulaExample()
    #parent.mathFormula.typeFormula('3.14 = \pi')
    parent.formulaWidget.setLayout(parent.mathFormula.getLayout())
    if totalHeight > 0:
        parent.formulaWidget.setMaximumHeight(totalHeight//6*2) # 2/6

    # Where answer will be displayed
    parent.answerWidget = QWidget()
    parent.answerWidget.setObjectName(u"answerWidget")
    parent.answerWidget.setStyleSheet("QWidget#answerWidget { border: 1px solid black; }")
    parent.tab1Layout.addWidget(parent.answerWidget, 2, 0, 1, 5) # row, column, rowSpan, columnSpan.
    # GraphLayout for results
    parent.answerFormula = GraphLayout(True)
    parent.answerFormula.setNormalText("Answer will appear here")
    parent.answerWidget.setLayout(parent.answerFormula.getLayout())
    if totalHeight > 0:
        parent.answerWidget.setMaximumHeight(totalHeight//6) # 1/6

    # keyboard grid widget 1. Special symbol keyboard
    parent.keyGridWidget1 = QWidget()
    parent.keyGridWidget1.setObjectName(u"keyGridWidget1")
    parent.tab1Layout.addWidget(parent.keyGridWidget1, 3, 0, 3, 5) # row, column, rowSpan, columnSpan.

    # keyboard grid 1
    parent.keyboardGrid1 = QGridLayout(parent.keyGridWidget1)
    parent.keyboardGrid1.setObjectName(u"keyboardGrid1")
    populateKeyBoardGrid(parent)
    if totalHeight > 0:
        parent.keyGridWidget1.setMaximumHeight(totalHeight//2) # 3/6

    # history list
    parent.histList = listelement.GraphList(parent.tab1, historyMode=True) # not ui thing
    parent.historyScroll = parent.histList.list_widget
    parent.historyScroll.setObjectName(u"historyScroll")
    parent.tab1Layout.addWidget(parent.historyScroll, 0, 5, 6, 3) # row, column, rowSpan, columnSpan. occupy whole column

    # Aktualnie wyświetlana formuła
    parent.current_expression = ""

    # Długości znaków z których składa się dana formuła
    parent.character_length = []

    # Umożliwienie wprowadzania formuł
    setupButtons(parent, mode = 1)

    # Dodajemy obsługę kliknięcia przycisku "="
    parent.tab1Buttons['='].clicked.connect(lambda: onEqualClick(parent))
    # Obsługa kliknięcia przycisku usuwającego ostatni znak
    parent.tab1Buttons['C'].clicked.connect(lambda: removeLastCharacter(parent, parent.mathFormula, mode = 1))
    # Obsługa kliknięcia przycisku usuwającego całe wyrażenie matematyczne
    parent.tab1Buttons['AC'].clicked.connect(lambda: removeExpression(parent, parent.mathFormula, mode = 1))
    # FIXME remove everything does not delete anything until something new is typed

    pass

def populateKeyBoardGrid(parent):
    "Populate keyboard grid in tab 1."
    #parent.tab1Buttons # buttons will be added to this dict

    scientifcKeyboard = [
        '.', '(', ')', 
        'sin', 'cos', 'tan', 'π',
        '^', 'sqrt', 'log', 'e', 'abs',
        'asin', 'acos', 'atan'
    ] + helpBT.inserter(
        [f'{x}' for x in range(10)], # lista cyfr
        [(1, '/'), (4+1, '*'), (7+2, '+'), (10+3, '-')] # te liczby: przed jaką cyfrą wstawić element, to po +: ile już wstawiono. 10 nie ma, ale chodzi o to, że za 9
    ) + ['C', 'AC'] + ['=']  

    keyboardMaker = helpBT.KeboardHelp(parent.keyboardGrid1, parent.tab1Buttons)
    keyboardMaker.addButtons(scientifcKeyboard, 4)

    pass