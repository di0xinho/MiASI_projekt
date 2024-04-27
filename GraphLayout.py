

from PySide6.QtWidgets import (QComboBox, QLabel,
    QPushButton, QSpinBox, QVBoxLayout, QHBoxLayout, QBoxLayout)

from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar

allActionsMap = {
    0:'Home',
	1:'Back',
	2:'Forward',
	3:'',
	4:'Pan',
	5:'Zoom',
	6:'Subplots',
	7:'Customize',
	8:'',
	9:'Save',
	10:''
}
"""Map of actions that `NavigationToolbar` contains by default"""

formulaActionKeys = [0,4,5,8,9,10]
"""Indexes of actions that toolbar for displaying math formulas should have."""

class GraphLayout:
    """This class is supposed to display Matplotlib's graph.
    Initialize it with first parameter set to true, if you want graph
    with graph navigation toolbar.\n
    - Use getLayout() to add it to parent layout.\n
    - Use formulaExample() to show example of using this as a display for math formulas written in LateX.\n
    - Use typeFormula() to display math formula.\n
    - Use draw() to refresh the view.\n
    - ax member can be used to adjust various graph or formula widget.\n
    - Use ax.clear() to clear display.\n
    When using formulaExample(), typeFormula() there's no need to call draw() nor clear().
    """
    __graphLayout = QVBoxLayout()
    
    def __init__(self, withToolbar = False) -> None:
        self.__populateGraphLayout(self.__graphLayout, withToolbar)
        self.ax = self.graph.figure.subplots()
        self.draw: function = self.graph.figure.canvas.draw
        self.draw()
        toolbar = self.graph_nav_menu
        removeActionsFromToolbar(toolbar,formulaActionKeys)
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
            self.graph_nav_menu = NavigationToolbar(self.graph) # , self.centralwidget
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

    def formulaExample(self):
        """
        You can directly use typeFormula().
        This only displays an example of using matplotlib for displaying math formulas.
        """
        self.__prepareFormulaExample()
        pass

    def __prepareFormulaExample(self):
        self.ax.clear()
        self.ax.axis('off')
        self.ax.text(0.5, 0.5, "$3.12^4$") # example of LateX text between $ signs
        #self.ax.tight()
        self.draw()
        pass

    def typeFormula(self, mathFormula: str):
        """Display math formula written in LateX format.
        """
        self.__setLatexText()
        pass

    def __setLatexText(self, latexText: str):
        """
        Instead of using widget for displaying graphs, use it for
        displaying mathematical formulas written in LateX.
        """
        print('Change text')
        try:
            self.ax.clear()
            self.ax.axis('off')
            self.ax.text(0.5, 0.5, f"${latexText}$", size=50, ha='center', va='center') # **kwargs: matplotlib.text.Text properties
            #self.ax.tight()
            self.draw()
        except:
            print("Some exception occurred") # Mostly 'unknown format, when expects LateX text, but unable to parse. Ex \p instead of \pi
        pass
    pass # end of GraphLayout

def getToolbarActions(toolbar: NavigationToolbar):
    """Get toolbar actions as strings"""
    actions = toolbar.actions()
    return [action.text() for action in actions]

def removeActionsFromToolbar(toolbar: NavigationToolbar, actionsToStay: list[int]):
    """Removes actions from toolbar which are not on given list.
    
    Parameters:
    - actionsToStay (list[int]): indexes of actions that won't get removed.
    You can check what index action have in `allActionsMap` defined on top of this file."""
    actions = toolbar.actions()
    for key in range(len(actions)):
        if key not in actionsToStay:
            toolbar.removeAction(actions[key])
    pass

def printBarActions(toolbar: NavigationToolbar):
    actions = toolbar.actions()
    for x in range(len(actions)):
        print(f"{x}: \'" + actions[x].text() + '\',')
    pass