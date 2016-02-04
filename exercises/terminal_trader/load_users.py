import sqlite3

class database:
	def __init__(self):
		self.dbname = 'stocks.db'
		

	def insert_user_data(self,name,uname,pwd,balance):
		self.conn = sqlite3.connect('stocks.db')
		self.name=name
		self.uname=uname
		self.pwd=pwd
		self.balance=balance

		self.conn.execute(
	    """
	    INSERT INTO users ("name","username","password","balance") VALUES(?,?,?,?)
	    
	    """,(self.name,self.uname,self.pwd,self.balance)
		)

		self.conn.commit()
		self.conn.close()


mydb = database()
with open('users.csv') as fp:
		for line in fp:
			line.rstrip()
			wrds = line.split(",")
			mydb.insert_user_data(wrds[0],wrds[1],wrds[2],wrds[3])
			