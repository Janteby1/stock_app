import sys
import pdb

class View ():

	def welcome(self):
		print ("")
		print ("Welcome to the trading game app!")
		print ("This app allows you to search for a company and get information back about it.")
		print ("You can search for a stock's live ticker price.")
		print ("After creating an account with a username and password you can start building your portfolio!")
		print ("Buy and sell stocks to try and make a profit.")
		print ("Lets get started ... ")
		print ("")

	def choice_login(self):
		choice = input ("Do you want to sign up [1] log in [2] or log in as an admin [3]?" )
		return choice

	def get_name (self):
		print ("")
		while True:
			name = input ("Welcome! Please enter your name: ")
			if name.isalpha():
				break
			else:
				self.get_name()
		return name

	def company_info(self,name,exchange,symbol):
		self.name = name
		self.exchange = exchange
		self.symbol = symbol
		print("")
		print('Name of the company: {}'.format(self.name))
		print('Exchange: {}'.format(self.exchange))
		print('Symbol: {}'.format(self.symbol))

	def get_username(self):
		print ("")
		while True:
			username = input ("Please enter a username: ")
			if username.isalpha() == True:
				break
			else:
				self.get_username()
		return username

	def get_password (self):
		print ("")
		while True:
			password = input ("Choose a password: ")
			if password.isalpha() == True:
				break
			else:
				self.get_password()
		return password

	def print_signup (self, name, username):
		print ("")
		print ("Welcome ", name)
		print ("You are currently logged in as: ", username)

	def admin_login(self):
		print("")
		print("Enter your admin login and userid: ")
		self.name = input("Login: ")
		self.pwd = input("Password: ")
		return (self.name, self.pwd)

	def login_username(self):
		print ("")
		self.name = input ("What is your name: ")
		self.username = input ("Please enter your username: ")
		return self.username

	def login_password(self):
		self.password = input ("Enter your password: ")
		return self.password

	def try_again (self):
		print ("We coult not find your username or password, please try again")

	def restart(self):
		print("")
		print ("Great! You created an account.")
		print ("Please restart and log back in.")
		print ("Thank you")

	def choose_option(self):
		print ("")
		print("What would you like to do?: ")
		print ("1. View a company stock price and live stock_quote ")
		print ("2. Buy a stock ")
		print ("3. Sell your stock ")
		print ("4. View your portfolio ")
		print ("5. Quit ")
		print ("")
		choice = input ("Enter the number of your choice: ")
		return choice

	def get_company (self):
		# need to fix this input
		print ("")
		while True:
			company = input ("Please enter a company: ")
			if company.isalpha() == True:
				break
			else:
				self.get_company()
		return company

	def get_stock (self):
		print ("")
		while True:
			stock = input ("Enter the companies stock symbol: ")
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

	def get_symbol(self):
		print ("")
		symbol = input("Enter the ticker symbol of the company you would you like to buy or sell: ")
		return(symbol)

	def get_num_shares(self):
		print ("")
		num = input("How many shares would you like to buy: ")
		return(num)

	def get_num_shares_to_sell(self):
		num = input("How many shares would you like to sell? ")
		return(num)

	def display_all_accounts(self, account_data):
		"""
		Prints all account data in a vertical list.
		"""
		print('Name - Amount')
		for pair in account_data:
			name, amount = pair
			print("{} - ${}".format(name, amount))

	def print_portfolio (self, portfolio):
		print ("Portfolio: ", portfolio)

		length = len(portfolio)
		print ("")
		print ("Your PortfolioView...")
		for i in range (0,length):
			print ("")
			# print ("User ID: ", stock_info['Name'])
			print ("Stock Symbol: ", portfolio[i][0])
			print ("Buy Price: ", portfolio[i][1])
			print ("Number of shares: ", portfolio[i][2])
			print ("User ID: ", portfolio[i][3])
			print ("")

