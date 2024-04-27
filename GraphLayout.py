

from PySide6.QtWidgets import (QComboBox, QLabel,
    QPushButton, QSpinBox, QVBoxLayout, QHBoxLayout, QBoxLayout)

from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar

# TODO for now you have to call formulaMode() every time you want to refresh formulaView, make it easier to use.
class GraphLayout:
    """This class is supposed to display Matplotlib's graph.\n
    Initialize it with second parameter set to true, if you want graph
    with graph navigation toolbar.\n
    Use getLayout() to add it to parent layout.\n
    Use formulaMode() to disable axles and use this as display for math formulas written in LateX.\n
    Use draw() to refresh the view.\n
    'ax' member can be used to adjust various graph or formula widget.
    """
    __graphLayout = QVBoxLayout()
    
    def __init__(self, withToolbar = False) -> None:
        self.__populateGraphLayout(self.__graphLayout, withToolbar)
        self.ax = self.graph.figure.subplots()
        self.draw: function = self.graph.figure.canvas.draw
        self.draw()
        pass

    def __populateGraphLayout(self, parentLayout: QBoxLayout, withToolbar: bool):
        """
        This function populates parentLayout with
        graph navigation Toolbar and graph itself.

        Parameters:
        - parentlayout: Layout to be populated with graph and toolbar.
        This Layout must be QHBoxLayout or QVBoxLayout.
        """
        # graph
        self.graph = FigureCanvas(Figure(figsize=(5, 3))) # graph
        self.graph.setObjectName(u"graph")
        
        # graph nav menu
        if withToolbar:
            self.graph_nav_menu = NavigationToolbar(self.graph, self.centralwidget)
            self.graph_nav_menu.setObjectName(u"graph_nav_menu")
            parentLayout.addWidget(self.graph_nav_menu)

        parentLayout.addWidget(self.graph)
        pass

    def getLayout(self):
        """Get layout, use it to add to parent widget or layout:\n
        >>> widget.setLayout(graphLayout.getLayout()) # for widgets
        >>> layout.addLayout(graphLayout.getLayout()) # for layouts
        """
        return self.__graphLayout

    def formulaMode(self):
        """Instead of using widget for displaying graphs, use it for
         displaying mathematical formulas."""
        self.__prepareFormulaView()
        pass

    def __prepareFormulaView(self):
        self.ax.axis('off')
        self.ax.text(0.5, 0.5, "$3.12^4$") # example of LateX text between $ signs
        self.tight()
        pass