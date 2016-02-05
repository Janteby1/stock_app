import sqlite3
import requests
import pdb

db = "stocks.db"
connection = sqlite3.connect(db)
c = connection.cursor()

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

	def create_user(self, name, username, password):
		c.execute("""
	        INSERT INTO users ("name", "username", "password") VALUES (?, ?, ?)""",(name, username, password))
		connection.commit()

	def print_user(self):
		cursor = connection.execute("SELECT name, username, password, permission FROM users")
		i =0
		while i < 1:
			for row in cursor:
				print (" ")
				print (" --- DATABASE ---")
				print ("Users")
				print ("NAME = ", row[0])
				print ("USERNAME = ", row[1])
				print ("PASSWORD = ", row[2], '\n')
			i +=1

	def check_login(self, username, password):
		info_list = []
		info_list = c.execute("""
			SELECT id FROM users WHERE username = ? AND password = ?""", (username, password))
		connection.commit()
		return info_list.fetchone() 

	def buy_stock(self, userid, acttype, balance):
		"Need to change the value of the balance in the user table then create the stock add the stock to his FK"
		pass
	
	def sell_stock(self, userid, stock_name, quantity):
        c.execute(
            """
            SELECT id, buyPrice, num
            FROM stock
            WHERE stockname = ? AND userid = ?""",
            (stockName, userid))
        available_stock = c.fetchone()
        if available_stock == []:
            print("You do not have this stock")
        stock_id, price, on_hand = available_stock
        if quantity > on_hand:
            print("Not enough stock available!")
            return

        c.execute(
            """
            UPDATE stock
            SET num = num - ?
            WHERE id = ?""",
            (quanity, stock_id))
        connection.commit()

        revenue = price * quality
        print("Stock sell sucessesful."
              "You have gained {}".format(revenue))

        c.execute(
            """
            UPDATE users
            SET balance = balance + ?
            WHERE id = ?""",
            (revenue, userid))
        connection.commit()
        return revenue

	def get_portfolio(self, name, username):
		"first fine user id from his name and username, then use this id to find all the stocks he has"
		portfolio = []
		c.execute("""
			SELECT * FROM stock where userid =(SELECT id FROM user WHERE name = ? AND username = ?"""), (name, username))
		return portfolio.fetchall() 
		connection.commit()

	def admin_view(self, userid, acttype, balance):
		"Need to select all stocks from all users, ordered by user name"
		pass
