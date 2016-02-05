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
			SELECT * FROM users WHERE username = ? AND password = ?""", (username, password))
		connection.commit()
		#return info_list.fetchone()
		return(info_list.fetchall()) 

	def buy_stock(self,stock,lastprice,num,userid,new_balance):
		self.stock=stock
		self.lastprice=lastprice
		self.num=num
		self.userid=userid
		self.new_balance=new_balance
		print('LastPrice  ',self.lastprice, '  ','user id ..',self.userid )

		c.execute("""
			INSERT INTO stock ("stockName","buyPrice","num","userid") VALUES(?,?,?,?)
	    
	    """,(self.stock,self.lastprice,self.num,self.userid)
		)

		c.execute("""
			UPDATE users SET balance=? WHERE id=?""",(self.new_balance, self.userid)
		)
		connection.commit()
		connection.close()

	