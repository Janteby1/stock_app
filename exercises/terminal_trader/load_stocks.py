import sqlite3

class database:
	def __init__(self):
		self.dbname = 'stocks.db'
		

	def insert_stock_data(self,name,buy_price,num,user_id):
		self.conn = sqlite3.connect('stocks.db')
		self.name=name
		self.buy_price=buy_price
		self.num=num
		self.user_id=user_id

		self.conn.execute(
	    """
	    INSERT INTO stock ("stockName","buyPrice","num","userid") VALUES(?,?,?,?)
	    
	    """,(self.name,self.buy_price,self.num,self.user_id)
		)

		self.conn.commit()
		self.conn.close()


mydb = database()
with open('stocks.csv') as fp:
		for line in fp:
			line.rstrip()
			wrds = line.split(",")
			mydb.insert_stock_data(wrds[0],wrds[1],wrds[2],wrds[3])
			