import sys
import pdb
from trader_views import *
from trader_models import *
# from trader_models.py import Model

class User ():
	def __init__ (self):
		self.view = View ()
		self.name = self.view.get_name
		self.username = username
		self.password = password


class Stock ():
	def __init__(self,name):
		self.name=name

	





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
