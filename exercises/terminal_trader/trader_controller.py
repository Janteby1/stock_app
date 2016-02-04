import sys
import pudb

from trader_views import View
from trader_models import Model

class User ():
	def __init__ (self):
		self.view = View ()
		self.name = self.view.get_name()
		print (self.name)
		# self.username = username
		# self.password = password


class Stock ():
	def __init__ (self):
		self.view = View ()
		self.model = Model()
		self.stock = self.view.get_stock()

	def get_stock_quote (self):
		stock_info = self.model.stock_info(self.stock)
		self.view.stock_quote(stock_info)


# class Run():
# 	def __init__ (self):

# 	def __repr__ (self):
# 		return str(self.value)

# 	def welcome (self):
# 		"Print a welcome statement"
# 		self.view.welcome()

user1 = User()
appl = Stock()
appl.get_stock_quote()

