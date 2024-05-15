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

def setupTab2(self):
    """
    Parameters:
    parent - Ui_Mainwindow class from ui_form.py
    """
    # create tab 2 widget
    self.tab2 = QWidget()
    self.tab2.setObjectName(u"tab2")
    self.tabWidget.addTab(self.tab2, "Wykresy (tab2)")
    self.tab2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    self.tab2Layout = QGridLayout()
    self.tab2.setLayout(self.tab2Layout)
    # nof columns and rows for tab2Layout. For now assume 8x6

    # function ScrollArea
    self.functionScroll = QScrollArea(self.tab2)
    self.functionScroll.setObjectName(u"functionScroll")
    self.functionScroll.setWidgetResizable(True) # ???
    self.tab2Layout.addWidget(self.functionScroll, 0, 0, 6, 3) # occupy whole column
    self.functionScrollContent = QWidget()
    self.functionScrollContent.setObjectName(u"functionScrollContents")
    self.functionScroll.setWidget(self.functionScrollContent)

    # Where function graphs will be displayed. This will be replaced by matplotlib widget.
    self.graphWidget = QWidget(self.tab2)
    self.graphWidget.setObjectName(u"graphWidget")
    self.tab2Layout.addWidget(self.graphWidget, 0, 3, 4, 5)

    # keyboard grid widget 2. Special symbol keyboard
    self.keyGridWidget2 = QWidget(self.tab2)
    self.keyGridWidget2.setObjectName(u"keyGridWidget2")
    self.tab2Layout.addWidget(self.keyGridWidget2, 4, 3, 2, 5)

    # keyboard grid 2
    self.keyboardGrid2 = QGridLayout(self.keyGridWidget2)
    self.keyboardGrid2.setObjectName(u"keyboardGrid2")
    self.populateKeyboardGrid2(self.keyboardGrid2)
    pass