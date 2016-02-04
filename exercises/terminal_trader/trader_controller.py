import sys
import pudb

from trader_views.py import View
# from trader_models.py import Model

class Run():
	def __init__ (self):
		# self.movie = None
		# self.id = None
		# self.view = View()
		# self.model= Model()

	def __repr__ (self):
		return str(self.value)

	def welcome (self):
		"Print a welcome statement"
		self.view.welcome()