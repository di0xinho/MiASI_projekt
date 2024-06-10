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

    # Where answer will be displayed. This will be replaced by matplotlib widget.
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
    populateKeyBoardGrid(parent, parent.keyboardGrid1)
    if totalHeight > 0:
        parent.keyGridWidget1.setMaximumHeight(totalHeight//2) # 3/6

    # history ScrollArea
    parent.historyScroll = QScrollArea()
    parent.historyScroll.setObjectName(u"historyScrollArea")
    parent.historyScroll.setWidgetResizable(True) # ???
    parent.tab1Layout.addWidget(parent.historyScroll, 0, 5, 6, 3) # row, column, rowSpan, columnSpan. occupy whole column
    parent.historyScrollContent = QWidget()
    parent.historyScrollContent.setObjectName(u"historyScrollAreaContents")
    parent.historyScroll.setWidget(parent.historyScrollContent)
    pass

def populateKeyBoardGrid(parent, keyboardGrid: QGridLayout):
    """Populate keyboard grid. First parameter is keyboardGrid reference. There are 3 ideas for second parameter:
        - pass tab number. 1 or 2
        - pass size keyboardGrid takes in its parent view
        - two different functions for two different tabs
        What about button names? Maybe pass also button list/tuple?
        """
    # some random buttons to populate keyboardGrid:
    
    # Co do ułamków, potęg i nawiasów - jeszcze nie dodaję tych guzików
    # FIXME where 0? 🤣
    parent.pushButtonOne = QPushButton("1")
    parent.pushButtonTwo = QPushButton("2")
    parent.pushButtonThree = QPushButton("3")
    parent.pushButtonFour = QPushButton("4")
    parent.pushButtonFive = QPushButton("5")
    parent.pushButtonSix = QPushButton("6")
    parent.pushButtonSeven = QPushButton("7")
    parent.pushButtonEight = QPushButton("8")
    parent.pushButtonNine = QPushButton("9")
    parent.pushButtonComma = QPushButton(".")
    parent.pushButtonFractions = QPushButton("Ułamek")
    parent.pushButtonPowers = QPushButton("Potęga")
    parent.pushButtonLeftBracket = QPushButton("(")
    parent.pushButtonRightBracket = QPushButton(")")
    parent.pushButtonSine = QPushButton("sin")
    parent.pushButtonCosine = QPushButton("cos")
    parent.pushButtonTangent = QPushButton("tan")
    parent.pushButtonLogarithms = QPushButton("log")
    parent.pushButtonSquareRoot = QPushButton("√")
    parent.pushButtonPi = QPushButton("π")
    parent.pushButtonEuler = QPushButton("e")
    parent.pushButtonAbsolute = QPushButton("abs")

    # adding buttons to keyboardGrid

    parent.keyboardGrid1.addWidget(parent.pushButtonFractions, 0, 2)
    parent.keyboardGrid1.addWidget(parent.pushButtonPowers, 0, 3)
    parent.keyboardGrid1.addWidget(parent.pushButtonLeftBracket, 0, 4)
    parent.keyboardGrid1.addWidget(parent.pushButtonRightBracket, 0, 5)
    parent.keyboardGrid1.addWidget(parent.pushButtonSine, 1, 2)
    parent.keyboardGrid1.addWidget(parent.pushButtonCosine, 1, 3)
    parent.keyboardGrid1.addWidget(parent.pushButtonTangent, 1, 4)
    parent.keyboardGrid1.addWidget(parent.pushButtonLogarithms, 2, 2)
    parent.keyboardGrid1.addWidget(parent.pushButtonSquareRoot, 2, 3)
    parent.keyboardGrid1.addWidget(parent.pushButtonPi, 2, 4)
    parent.keyboardGrid1.addWidget(parent.pushButtonEuler, 3, 2)
    parent.keyboardGrid1.addWidget(parent.pushButtonAbsolute, 3, 3)
    parent.keyboardGrid1.addWidget(parent.pushButtonComma, 3, 4)
    parent.keyboardGrid1.addWidget(parent.pushButtonOne, 4, 2)
    parent.keyboardGrid1.addWidget(parent.pushButtonTwo, 4, 3)
    parent.keyboardGrid1.addWidget(parent.pushButtonThree, 4, 4)
    parent.keyboardGrid1.addWidget(parent.pushButtonFour, 5, 2)
    parent.keyboardGrid1.addWidget(parent.pushButtonFive, 5, 3)
    parent.keyboardGrid1.addWidget(parent.pushButtonSix, 5, 4)
    parent.keyboardGrid1.addWidget(parent.pushButtonSeven, 6, 2)
    parent.keyboardGrid1.addWidget(parent.pushButtonEight, 6, 3)
    parent.keyboardGrid1.addWidget(parent.pushButtonNine, 6, 4)
    

    pass