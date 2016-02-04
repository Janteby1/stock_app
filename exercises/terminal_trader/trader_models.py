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
