import sqlite3
import requests
import pdb

class Model:
	# def __init__(self):
		# self.stock_name=name
		#self.apiname = 'http://dev.markitondemand.com/MODApis/#doc_lookup'

	def search_company(self, company):
		''' get company information'''
		stock_company = requests.get("http://dev.markitondemand.com/Api/v2/Lookup/json?input=%s" % (company)).json() 
		return(stock_company)

	def stock_info(self, stock):
		stock_info = requests.get("http://dev.markitondemand.com/Api/v2/Quote/json?symbol=%s" %(stock)).json()
		return stock_info
