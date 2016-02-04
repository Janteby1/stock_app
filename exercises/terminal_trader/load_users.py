class database:
	def __init__(self):
		self.dbname = 'stocks.db'
		self.conn = sqlite3.connect('stocks.db')

	def insert_user_data(self,uname,pwd,balance):
		self.uname=uname
		self.pwd=pwd
		self.balance=balance

		self.conn.execute(
	    """
	    INSERT INTO users ("username","password","balance") VALUES(?,?,?)
	    
	    """,(self.uname,self.pwd,self.balance)
		)

		self.conn.commit()
		conn.close()


with open('users.csv') as fp:
		for line in fp:
			line.rstrip()
			wrds = line.split(",")
			mydb.insert_employee_data(wrds[0],wrds[1],wrds[2])
			