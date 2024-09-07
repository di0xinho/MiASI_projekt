from constants import MAINFILE
if __name__ == "__main__":
    print(f"\nTo start calculator run {MAINFILE} file.\n")
    exit(0)

from PySide6.QtCore import QSize, Qt
#from PySide6.QtGui import 
from PySide6.QtWidgets import (QPushButton, QScrollArea, QHBoxLayout,
	QSizePolicy, QStatusBar, QWidget, QListWidgetItem, QListWidget, QCheckBox)
from graphlayout import GraphLayout

funexample = "f(x) = 38 * 5 / 7 * \pi * \cos(54) - 783314 + 4,5 * 10^{12} + 38 * 5 / 7 * \pi * \cos(54) - 783314 + 4,5 * 10^{12}"
funbegin = "f(x) = "
histexample = 'result'

# tworzy widget
def prepareWidgetFunc(n) -> QWidget:
	"""Widget listing function formulas.
	Widget will be horizontal box with checkbox, formula and options (3 dots)"""
	widget = QWidget()
	layout = QHBoxLayout()
	check = QCheckBox(f"f_{n}")
	check.setMaximumSize(QSize(80, 120))
	grLayout = GraphLayout()
	grLayout.typeFormula(funexample, 12, 'left', True)
	layout.addWidget(check)
	grLayout.graph.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
	layout.addWidget(grLayout.graph)
	#layout.addLayout(grLayout.getLayout())
	widget.setLayout(layout)
	widget.setMaximumHeight(120)
	# TODO add buttons such as edit, delete, color?
	return widget

def prepareWidgetHist(n) -> QWidget:
	"""Widget listing calculation history.
	Widget will be horizontal box with calculated result and options (3 dots)"""
	widget = QWidget()
	layout = QHBoxLayout()
	grLayout = GraphLayout()
	grLayout.typeFormula(histexample, 12, 'left', True)
	grLayout.graph.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
	layout.addWidget(grLayout.graph)
	#layout.addLayout(grLayout.getLayout())
	widget.setLayout(layout)
	widget.setMaximumHeight(120)
	# TODO add button to copy or delete
	return widget

# TODO align text to left

# lista wyników albo funkcji - historyList, graphList
class GraphList: # misleading name
	"List of graphs. Can be used to display calc history or function formulas"
	def __init__(self, parent, historyMode=False):
		self.list_widget = QListWidget(parent)
		self.history_mode=historyMode
		self.widgets = []

	def prepareFuncExample(self):
		for i in range(3):
			widget = prepareWidgetFunc(i)
			self.addWidget(widget)
		pass
	def prepareHistExample(self):
		for i in range(3):
			widget = prepareWidgetHist(i)
			self.addWidget(widget)
		pass

	# dodaj element do listy
	def addWidget(self, widget: QWidget):
		"Add widget to list in interface. Works for both history and functions"
		self.widgets.append(widget)
		item = QListWidgetItem(self.list_widget)
		item.setTextAlignment(Qt.AlignmentFlag.AlignLeft)
		item.setSizeHint(QSize(self.list_widget.sizeHint().width(), widget.size().height()))
		self.list_widget.setItemWidget(item, widget)
		pass
	def editWidget(self):
		"when listing functions, there is an option to enter edit mode, to edit function"
		pass
	def deleteWidget(self):
		"simply delete from list"
		pass
	pass

# TODO element listy z wszystkimi feature'ami wypisanymi poniżej

# ✔

# to będzie klasa, która umożliwi wyświetlenie jakiejś formuły mat (wyniki z historii obliczeń / funkcje)
# jako element listy.

# ogólne opcje:
# - wyświetlanie formuły, 1 lub 2
# - stały tekst na początku, jak np. f(x)=
# - możliwość dołożenia przycisków / dropdown
# - opcja usuń

# Usuń, możliwe rozwiązania: Albo prawym i wybrać usuń, albo przycisk z symbolem kosza albo X.
# albo dropdown menu pod prawym przyciskiem, albo przyciski z ikonkami

# te mogą być w oddzielnych dziedziczących z tego klasach:

# opcje historii:
# - kliknij, aby skopiować wynik

# opcje listy wykresów:
# - checkbox - kontroluje widoczność na wykresie. Może zamiast tego wyszarzanie pod lewym przyciskiem myszy?
# - edytuj (button lub w dropdownie)
# - może pole z kolorem?
