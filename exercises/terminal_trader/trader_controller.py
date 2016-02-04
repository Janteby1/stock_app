import sys
import pdb
from trader_views import *
from trader_models import *
# from trader_models.py import Model

class User ():
	def __init__ (self):
		self.view = View ()
		self.name = self.view.get_name()
		self.username = self.view.get_username()
		self.password = self.view.get_password()
		self.view.print_login(self.name, self.username)

class Stock ():
	def __init__ (self):
		self.view = View ()
		self.model = Model()
		self.company = self.view.get_company()

	def get_company_info (self):
		response = self.model.search_company(self.company)
		dictt = response[0]
		self.view.company_info(dictt['Name'],dictt['Exchange'],dictt['Symbol'])

	def get_stock_quote (self):
		self.stock = self.view.get_stock()
		stock_info = self.model.stock_info(self.stock)
		self.view.stock_quote(stock_info)


# class Run():
# 	def __init__ (self):

# name='Apple'
# mystock = Stock(name)
# myapi = Api(name)

user1 = User()
appl = Stock()
appl.get_company_info()	
appl.get_stock_quote()

