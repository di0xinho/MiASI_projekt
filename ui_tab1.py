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

# historyScroll and functionScroll will contain dynamically set Widgets with GraphLayout

# FIXME The GraphLayout ignores proportions. For now I don't know how to fix this.

# TODO GraphLayout can be GraphWidget instead of wrapping GraphLayout in additional widget every time.

def setupTab1(parent):
    """
    Parameters:
    parent - Ui_Mainwindow class from ui_form.py
    """
    parent.tab1 = QWidget()
    parent.tab1.setObjectName(u"tab1")
    parent.tabWidget.addTab(parent.tab1, "Naukowy (tab1)")
    parent.tab1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    parent.tab1Layout = QGridLayout()
    parent.tab1.setLayout(parent.tab1Layout)
    # nof columns and rows for tab1Layout. For now assume 8x6

    # Widget to hold GraphLayout
    parent.formulaWidget = QWidget()
    parent.formulaWidget.setObjectName(u"formulaWidget")
    parent.formulaWidget.setStyleSheet("QWidget#formulaWidget { border: 1px solid black; }")
    parent.tab1Layout.addWidget(parent.formulaWidget, 0, 0, 2, 5) # row, column, rowSpan, columnSpan. For some reason positional arguments don't work here
    # GraphLayout for input
    parent.mathFormula = GraphLayout(True)
    parent.mathFormula.formulaExample()
    parent.formulaWidget.setLayout(parent.mathFormula.getLayout())

    # Where answer will be displayed. This will be replaced by matplotlib widget.
    parent.answerWidget = QWidget()
    parent.answerWidget.setObjectName(u"answerWidget")
    parent.formulaWidget.setStyleSheet("QWidget#answerWidget { border: 1px solid black; }")
    parent.tab1Layout.addWidget(parent.answerWidget, 2, 0, 1, 5) # row, column, rowSpan, columnSpan.
    # GraphLayout for results
    parent.answerFormula = GraphLayout(True)
    parent.answerFormula.formulaExample()
    parent.formulaWidget.setLayout(parent.answerFormula.getLayout())

    # keyboard grid widget 1. Special symbol keyboard
    parent.keyGridWidget1 = QWidget()
    parent.keyGridWidget1.setObjectName(u"keyGridWidget1")
    parent.tab1Layout.addWidget(parent.keyGridWidget1, 3, 0, 3, 5) # row, column, rowSpan, columnSpan.

    # keyboard grid 1
    parent.keyboardGrid1 = QGridLayout(parent.keyGridWidget1)
    parent.keyboardGrid1.setObjectName(u"keyboardGrid1")
    parent.populateKeyBoardGrid(parent.keyboardGrid1)

    # history ScrollArea
    parent.historyScroll = QScrollArea()
    parent.historyScroll.setObjectName(u"historyScrollArea")
    parent.historyScroll.setWidgetResizable(True) # ???
    parent.tab1Layout.addWidget(parent.historyScroll, 0, 5, 6, 3) # row, column, rowSpan, columnSpan. occupy whole column
    parent.historyScrollContent = QWidget()
    parent.historyScrollContent.setObjectName(u"historyScrollAreaContents")
    parent.historyScroll.setWidget(parent.historyScrollContent)
    pass