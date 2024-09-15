from constants import MAINFILE
if __name__ == "__main__":
    print(f"\nTo start calculator run {MAINFILE} file.\n")
    exit(0)

from PySide6.QtWidgets import (QComboBox, QLabel,
    QPushButton, QSpinBox, QVBoxLayout, QHBoxLayout, QBoxLayout, QMessageBox)

from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar

# used for plot example and plotting
import sympy as sp
import numpy as np

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

formulaActionKeys = [0,4,8] # ,9,10
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
    
    def __init__(self, withToolbar = False, plotMode = False) -> None:
        self.withToolbar = withToolbar
        self.shortToolbar = True
        self.currentFormula = ""  
        if plotMode:
            self.shortToolbar = False
            # connected 'xlim_changed' callback to GraphLayout.redrawPlot() in MainWindow. For some reason it has to be this way :/
        self.__graphLayout = QVBoxLayout()
        self.__populateGraphLayout(self.__graphLayout)
        self.ax = self.graph.figure.subplots()
        self.draw: function = self.graph.figure.canvas.draw
        self.draw()
        if self.withToolbar:
            toolbar = self.graph_nav_menu
            if self.shortToolbar:
                removeActionsFromToolbar(toolbar, formulaActionKeys)
        pass

    def listMode(self):
        # withToolbar = False
        # smaller font!
        # smaller size!
        pass

    def plotMode(self):
        # withToolbar = True
        # shortToolbar = False
        pass

    def mathMode(self):
        # withToolbar = True
        # shortToolbar = True
        pass

    # Getter dla formuły
    def getFormula(self) -> str:
        """Zwraca ostatnio ustawioną formułę."""
        return self.currentFormula

    def __populateGraphLayout(self, parentLayout: QBoxLayout):
        """
        This function populates parentLayout with
        graph navigation Toolbar and graph itself.

        Parameters:
        - parentlayout: Layout to be populated with graph and toolbar.
        This Layout must be QHBoxLayout or QVBoxLayout.
        """
        # graph
        #self.graph = FigureCanvas(Figure(figsize=(5, 3))) # graph
        self.graph = FigureCanvas(Figure(figsize=(3, 1))) # graph
        self.graph.setObjectName(u"graph")

        # graph nav menu
        if self.withToolbar:
            self.graph_nav_menu = NavigationToolbar(self.graph) # , self.centralwidget
            self.graph_nav_menu.setObjectName(u"graph_nav_menu")
            self.graph_nav_menu.setMaximumWidth(280)
            if self.shortToolbar:
                self.graph_nav_menu.setMaximumWidth(100)
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
        self.ax.text(0.5, 0.5, "$3.12^4$", size = 20) # example of LateX text between $ signs
        #self.ax.tight()
        self.draw()
        pass

    def typeFormula(self, mathFormula: str, fontSize=20, alignText='center', toLeft=False):
        """
        Display math formula written in LateX format.
        Instead of using widget for displaying graphs, use it for
        displaying mathematical formulas written in LateX.
        \nalign text: 'left' / 'center' / 'right'
        """
        
        latexText = mathFormula
        try:
            
            self.ax.clear()
            self.ax.axis('off')
            x = 0.5
            if toLeft:
                x = -0.15
            self.ax.text(x, 0.5, f"${latexText}$", size=fontSize, ha=alignText, va='center') # **kwargs: matplotlib.text.Text properties
            #self.ax.tight()
            self.draw()
            self.currentFormula = latexText
            if '=' in self.currentFormula:
                self.currentFormula = self.currentFormula.split('=')[0].strip()
        except:
            print("Some exception occurred") # Mostly 'unknown format, when expects LateX text, but unable to parse. Ex \p instead of \pi
        pass
    pass # end of GraphLayout

    def setNormalText(self, text: str, fontSize=20):
        """
        This can be used to set some hints.
        For setting math formulas use typeFormula
        """
        #print('Change text')
        try:
            self.ax.clear()
            self.ax.axis('off')
            self.ax.text(0.5, 0.5, f"{text}", size=fontSize, ha='center', va='center') # **kwargs: matplotlib.text.Text properties
            self.ax.tight()
            self.draw()
        except:
            #print("Some exception occurred")
            pass
        pass

    def plotExample(self):
        # clear:
        self.ax.clear()
        # example:
        x = sp.symbols('x')  # variable
        # f = sp.sin(x) + sp.cos(x)  # function
        f = sp.sin(x)

        self.setPlot(x, f)
        pass

    # TODO can it draw multiple functions??

    def setPlot(self, sympy_var, sympy_fun, color='red'):
        'sympy_var - example: sp.symbols(\'x\'), sympy_fun - sympy function'
        # convert to numeric
        f_num = sp.lambdify(sympy_var, sympy_fun)
        self.f_num = f_num
        self.f_col = color # TODO przypisywanie kolorów, bez tego przy przesuwaniu wykresu kolor się bardzo szybko zmienia
        x_vals = np.linspace(-10, 10, 10000) # begin view with x from -10 to 10 visible
        y_vals = f_num(x_vals)
        
        # plot
        self.ax.plot(x_vals, y_vals, color = self.f_col)
        self.ax.set_xlabel('x',)
        self.ax.set_ylabel('f(x)')
        self.ax.set_title('Plot of f(x)')
        self.draw()
        pass

    def redrawPlot(self):
        "when graph view is moved it has to be redrawn"
        if self.f_num is None:
            return
        minx, maxx = self.ax.get_xlim()
        x_vals = np.linspace(minx, maxx, 3840)
        y_vals = self.f_num(x_vals)

        # plot
        self.ax.plot(x_vals, y_vals, color = self.f_col)
        self.ax.set_xlabel('x',)
        self.ax.set_ylabel('f(x)')
        self.ax.set_title('Plot of f(x)')
        self.draw()
        pass
    pass # end of GraphLayout

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
