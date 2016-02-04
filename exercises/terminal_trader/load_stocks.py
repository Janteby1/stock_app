class database:
	def __init__(self):
		self.dbname = 'stocks.db'
		self.conn = sqlite3.connect('stocks.db')

	def insert_stock_data(self,name,buy_price,num,user_id):
		self.name=name
		self.buy_price=buy_price
		self.num=num
		self.user_id=user_id

		self.conn.execute(
	    """
	    INSERT INTO stocks ("name","buyprice","num","user_id") VALUES(?,?,?,?)
	    
	    """,(self.name,self.buy_price,self.num,self.user_id)
		)

		self.conn.commit()
		conn.close()


with open('stocks.csv') as fp:
		for line in fp:
			line.rstrip()
			wrds = line.split(",")
			mydb.insert_stock_data(wrds[0],wrds[1],wrds[2],wrds[3])
			