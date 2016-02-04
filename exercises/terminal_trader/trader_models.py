<<<<<<< HEAD
import sqlite3
import requests
import pdb

class Api():
	def __init__(self,name):
		self.stock_name=name
		#self.apiname = 'http://dev.markitondemand.com/MODApis/#doc_lookup'

	def search_company(self):
		''' get company information'''
		stock_company = requests.get("http://dev.markitondemand.com/Api/v2/Lookup/json?input=%s" % (self.stock_name)).json() 
		return(stock_company)
=======
import requests
import pudb 

class Model:
	# do I neeed an init ?!

	def stock_info(self, stock):
		stock_info = requests.get("http://dev.markitondemand.com/Api/v2/Quote/json?symbol=%s" %(stock)).json()
		return stock_info
>>>>>>> master
