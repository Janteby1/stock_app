import sys
import pudb

class View ():

	def welcome (self):
		print ("Hello")
		print ("Welcome to the trading game app!")
		print ("This app allows you to search for a company and get information back about it.")
		print ("You can search for a stock's live ticker price.")
		print ("After creating an account with a username and password you can start building your portfolio!")
		print ("Buy and sell stocks to try and make a profit.")
		print ("Lets get started ... ")

	def get_name (self):
		print ("")
		while True:
			name = input ("Welcome! Please enter your name: ")
			if name.isalpha() == True:
				break
			else:
				self.get_name()
		return name

	def get_stock (self):
		print ("")
		while True:
			stock = input ("Welcome! Please enter a stock symbol: ")
			if stock.isalpha() == True:
				break
			else:
				self.get_stock()
		return stock

	def stock_quote (self, stock_info):
		print ("")
		# print (stock_info)
		print ("Printing Live Quote...")
		print ("")
		print ("Name: ", stock_info['Name'])
		print ("Symbol: ", stock_info["Symbol"])
		print ("LastPrice: ", stock_info["LastPrice"])
		print ("Timestamp: ", stock_info["Timestamp"])
		print ("Open: ", stock_info["Open"])
		print ("Change: ", stock_info["Change"])
		print ("High: ", stock_info["High"])
		print ("Low: ", stock_info["Low"])
		print ("ChangeYTD: ", stock_info["ChangeYTD"])
		print ("")


