from constants import MAINFILE
if __name__ == "__main__":
    print(f"\nTo start calculator run {MAINFILE} file.\n")
    exit(0)

from PySide6.QtCore import QSize, Qt
#from PySide6.QtGui import 
from PySide6.QtWidgets import (QPushButton, QScrollArea, QHBoxLayout,
	QSizePolicy, QStatusBar, QWidget, QListWidgetItem, QListWidget, QCheckBox)
from graphlayout import GraphLayout

funbegin = "f(x) = 38 * 5 / 7 * \pi * \cos(54) - 783314 + 4,5 * 10^{12} + 38 * 5 / 7 * \pi * \cos(54) - 783314 + 4,5 * 10^{12}"

# tworzy widget
def prepareWidget(n) -> QWidget:
	"Widget will be horizontal box with checkbox, formula and options (3 dots)"
	widget = QWidget()
	layout = QHBoxLayout()
	check = QCheckBox(f"f_{n}")
	check.setMaximumSize(QSize(80, 120))
	grLayout = GraphLayout()
	grLayout.typeFormula(funbegin, 12, 'left', True)
	layout.addWidget(check)
	grLayout.graph.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
	layout.addWidget(grLayout.graph)
	#layout.addLayout(grLayout.getLayout())
	widget.setLayout(layout)
	widget.setMaximumHeight(120)
	# TODO add buttons such as edit, delete, color?
	return widget

# TODO align text to left

# lista wyników albo funkcji - historyList, graphList
class GraphList: # misleading name
	"List of graphs. Can be used to display calc history or function formulas"
	def __init__(self, parent):
		self.list_widget = QListWidget(parent)
		print('list size:', self.list_widget.size(), 'list hint: ', self.list_widget.sizeHint())
		self.widgets = []
	def prepareExample(self):
		for i in range(3):
			widget = prepareWidget(i)
			self.widgets.append(widget)
			self.addWidget(widget)
		pass
	# dodaj element do listy
	def addWidget(self, widget: QWidget):
		"add widget to list in interface"
		item = QListWidgetItem(self.list_widget)
		item.setTextAlignment(Qt.AlignmentFlag.AlignLeft)
		item.setSizeHint(QSize(self.list_widget.sizeHint().width(), widget.size().height()))
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
