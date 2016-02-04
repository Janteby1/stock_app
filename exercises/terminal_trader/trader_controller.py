import sys
<<<<<<< HEAD
import pdb
from trader_views import *
from trader_models import *
# from trader_models.py import Model
=======
import pudb

from trader_views import View
from trader_models import Model
>>>>>>> master

class User ():
	def __init__ (self):
		self.view = View ()
		self.name = self.view.get_name()
		self.username = self.view.get_username()
		self.password = self.view.get_password()
		self.view.print_login(self.name, self.username)

class Stock ():
<<<<<<< HEAD
	def __init__(self,name):
		self.name=name

	
=======
	def __init__ (self):
		self.view = View ()
		self.model = Model()
		self.stock = self.view.get_stock()

	def get_stock_quote (self):
		stock_info = self.model.stock_info(self.stock)
		self.view.stock_quote(stock_info)
>>>>>>> master


# class Run():
# 	def __init__ (self):

<<<<<<< HEAD


#class Run():
#	def __init__ (self):

#	def __repr__ (self):
#		return str(self.value)

#	def welcome (self):
#		"Print a welcome statement"
#		self.view.welcome()

name='Apple'
mystock = Stock(name)
myapi = Api(name)
response = myapi.search_company()
dictt = response[0]
View.company_info(dictt['Name'],dictt['Exchange'],dictt['Symbol'])
=======
# 	def __repr__ (self):
# 		return str(self.value)

# 	def welcome (self):
# 		"Print a welcome statement"
# 		self.view.welcome()

user1 = User()
appl = Stock()
appl.get_stock_quote()

>>>>>>> master
