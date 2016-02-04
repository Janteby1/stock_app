import sys
import pdb

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


	def company_info(self,name,exchange,symbol):
		self.name=name
		self.exchange=exchange
		self.symbol = symbol
		print("")
		print('Name of the company ..{} Exchange..{} and symbol..{}'.format(self.name,self.exchange,self.symbol))



