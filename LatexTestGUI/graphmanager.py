
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.markers import MarkerStyle
from matplotlib.backends.backend_qtagg import FigureCanvas # ???
from numpy import array as nparray


class GraphManager:
	ax: Axes
	def __init__(self, figcanv: FigureCanvas):
		fig: Figure = figcanv.figure
		self.ax = fig.subplots()
		#self.cidpress = fig.canvas.mpl_connect('button_press_event', self.on_press) # has to keep reference
		self.draw: function = fig.canvas.draw # reference to method for redrawing graph
		self.tight: function = fig.tight_layout # makes graph take more space that would be empty otherwise

		# Alternatively to draw, I could have programatically press home button on graph toolbar
		# create graphs using ax.plot() or ax.scatter()
		pass

	def prepareFormulaView(self):
		self.ax.axis('off')
		self.ax.text(0.5, 0.5, "$3.12^4$") # LateX text between $ signs
		self.tight()
		pass

	def setLatexText(self, latexText: str):
		print('Change text')
		try:
			self.ax.clear()
			self.ax.axis('off')
			self.ax.text(0.5, 0.5, f"${latexText}$", size=50, ha='center', va='center') # **kwargs: matplotlib.text.Text properties
			self.tight()
			self.draw()
		except:
			print("Some exception occurred") # Mostly 'unknown format, when expects LateX text, but unable to parse. Ex \p instead of \pi
		pass
