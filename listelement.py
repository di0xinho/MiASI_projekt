
from PySide6.QtWidgets import (QPushButton, QScrollArea, QHBoxLayout,
	QSizePolicy, QStatusBar, QWidget, QListWidgetItem, QListWidget, QCheckBox)
from graphlayout import GraphLayout

funbegin = "f(x) = "

# tworzy widget
def prepareWidget(n):
	"Widget will be horizontal box with checkbox, formula and options (3 dots)"
	widget = QWidget()
	layout = QHBoxLayout()
	check = QCheckBox(f"I'm no.{n}")
	#grLayout = GraphLayout()
	#grLayout.typeFormula(funbegin)
	layout.addWidget(check)
	#layout.addWidget(grLayout)
	widget.setLayout(layout)
	return widget

# lista wyników albo funkcji - historyList, graphList
class GraphList: # misleading name
	"List of graphs. Can be used to display calc history or function formula"
	def __init__(self, parent):
		self.list_widget = QListWidget(parent)
		self.widgets = []
	def prepareExample(self):
		for i in range(3):
			widget = prepareWidget(i)
			self.widgets.append(widget)
			self.addWidget(widget)
		pass
	# dodaj element do listy
	def addWidget(self, widget):
		item = QListWidgetItem(self.list_widget)
		item.setSizeHint(widget.sizeHint()) # ?
		self.list_widget.setItemWidget(item, widget)
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