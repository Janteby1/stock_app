import sys
import pdb
from trader_views import *
from trader_models import *
# from trader_models.py import Model

class User():
	def __init__ (self):
		self.view = View ()
		self.model = Model()

	def choice_login (self):
		self.view.welcome()
		choice = self.view.choice_login()
		if choice == "1":
			self.signup()
		elif choice == "2":
			self.login()
		else:
			self.choice_login() 

	def signup (self):
		name = self.view.get_name()
		username = self.view.get_username()
		password = self.view.get_password()
		# self.view.print_signup(self.name, self.username)
		"send the values to the db"
		self.model.create_user(name, username, password)
		self.view.restart()
		sys.exit()

	def login (self):
		username = self.view.login_username()
		password = self.view.login_password()
		self.info_list = self.model.check_login (username, password)
		if self.info_list is not None:
			print ("Welcome back to the stock trading game!")
		else:
			self.view.try_again()
			sys.exit()
			# need to get this to loop

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
		# get the users name and username and pass it to the check_balance function
		portfolio = self.model.check_balance('''---''')
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
		num = self.view.get_num_shares()
		total_price_of_shares = int(num) * int(self.stock_info['LastPrice'])
		if user1.info_list[0][4] == None:
			print ("Sorry! You are currently out of funds.")
			print ("")
		else:
			new_balance = int(user1.info_list[0][4]) - total_price_of_shares
			self.model.buy_stock(self.stock_info['Name'],self.stock_info['LastPrice'],num,user1.info_list[0][0],new_balance)
		user1.choose_option()


# class Run():
# 	def __init__ (self):

# name='Apple'
# mystock = Stock(name)
# myapi = Api(name)

user1 = User()
user1.choice_login()
stock = Stock()
user1.choose_option()

# stock.get_company_info()	
# stock.get_stock_quote()
# stock.buy_stocks()
# stock.sell_stocks()

