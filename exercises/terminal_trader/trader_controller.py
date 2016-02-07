import sys
import pdb
from trader_views import *
from trader_models import *

class User():
	def __init__ (self):
		self.view = View()
		self.model = Model()
		self.admin = Admin()

	def login_admin(self):
		return_adminlst = self.view.admin_login()
		self.model.check_login(return_adminlst[0], return_adminlst[1])
		self.admin.viewall()

	def choice_login (self):
		self.view.welcome()
		choice = self.view.choice_login()
		if choice == "1":
			self.signup()
		if choice == "2":
			self.login()
		if choice == "3":
			self.login_admin()
		else:
			self.choice_login() 

	def signup (self):
		name = self.view.get_name()
		username = self.view.get_username()
		password = self.view.get_password()
		balance = 10000.00
		"send the values to the db"
		self.model.create_user(name, username, password, balance)
		self.view.restart()
		sys.exit()

	def login (self):
		self.username = self.view.login_username()
		self.password = self.view.login_password()
		self.info_list = self.model.check_login (self.username, self.password)
		if self.info_list is not None:
			print ("")
			print ("Welcome back to the stock trading game!")
			balance = self.model.get_balance(self.username, self.password)
			print ("Your current balance is: ", balance, "dollars.")
		else:
			self.view.try_again()
			sys.exit()

	def choose_option (self):
		choice = self.view.choose_option()
		if choice == "1":
			stock.get_company_info()	
			stock.get_stock_quote()
		elif choice == "2":
			stock.buy_stocks()
		elif choice == "3":
			stock.sell_stocks()
		elif choice == "4":
			self.get_portfolio()
		elif choice == "5":
			print ("Goodbye.")
			sys.exit()
		else:
			print ("Please enter a valid choice. (1, 2, 3 or 4) ")
			self.choose_option()

	def get_portfolio (self):
		portfolio = self.model.get_portfolio(self.username, self.password)
		self.view.print_portfolio(portfolio)
		self.choose_option()

class Stock():
	def __init__ (self):
		self.view = View ()
		self.model = Model()

	def get_company_info (self):
		self.company = self.view.get_company()
		response = self.model.search_company(self.company)
		dictt = response[0]
		self.view.company_info(dictt['Name'],dictt['Exchange'],dictt['Symbol'])

	def get_stock_quote (self):
		self.stock = self.view.get_stock()
		self.stock_info = self.model.stock_info(self.stock)
		self.view.stock_quote(self.stock_info)
		user1.choose_option()

	def buy_stocks (self):
		symbol = self.view.get_symbol()
		num = self.view.get_num_shares()
		if user1.info_list[0][4] == None:
			print ("Sorry! You are currently out of funds.")
			print ("")
		else:
			self.model.buy_stock(symbol, num, user1.info_list[0][0])
			user1.choose_option()

	def sell_stocks(self):
		symbol = self.view.get_symbol()
		num = self.view.get_num_shares_to_sell()
		self.model.sell_stock(symbol,num,user1.info_list[0][0])


user1 = User()
user1.choice_login()
stock = Stock()
user1.choose_option()
