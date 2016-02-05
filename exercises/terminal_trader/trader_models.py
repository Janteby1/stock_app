import sqlite3
import requests
import pdb

db = "stocks.db"
connection = sqlite3.connect(db)
c = connection.cursor()

class Model:
    def search_company(self, company):
        ''' get company information'''
        stock_company = requests.get("http://dev.markitondemand.com/Api/v2/Lookup/json?input=%s" % (company)).json() 
        return(stock_company)

    def stock_info(self, stock):
        stock_info = requests.get("http://dev.markitondemand.com/Api/v2/Quote/json?symbol=%s" %(stock)).json()
        return stock_info

    def create_user(self, name, username, password, balance):
        c.execute("""
            INSERT INTO users ("name", "username", "password", "balance") VALUES (?, ?, ?, ?)""",(name, username, password, balance))
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
        return(info_list.fetchall()) 

    def get_balance(self, username, password):
        balance = c.execute("""
            SELECT balance FROM users WHERE username = ? AND password = ?""", (username, password))
        connection.commit()
        return balance.fetchone()

    def buy_stock(self,symbol,num,userid):
        "Need to change the value of the balance in the user table then create the stock add the stock to his FK"
        self.symbol=symbol
        self.num=num
        self.userid=userid

        info_list =[]
        info_list = self.stock_info(symbol)

        self.lastprice=info_list["LastPrice"]
        print('buy Price  ',self.lastprice, '  ','user id ..',self.userid )

        total_price_of_shares = int(num) * int(self.lastprice)

        c.execute("""
            INSERT INTO stock ("stockName","buyPrice","num","userid") VALUES(?,?,?,?)
        
        """,(self.symbol,self.lastprice,self.num,self.userid)
        )

        c.execute("""
            UPDATE users SET balance=balance - ? WHERE id=?""",(total_price_of_shares, self.userid)
        )
        print ("Your purchase ahs went through")
        connection.commit()
        connection.close()
    
    def sell_stock(self, symbol,quantity,userid):
        self.symbol= symbol
        self.quantity=quantity
        self.userid=userid

        info_list = []
        info_list = self.stock_info(self.symbol)
        self.lastprice=info_list["LastPrice"]
        print('Sell price', self.lastprice, ' ', 'user id..', self.userid )
        total_revenue = int(num) * int(self.lastprice)


        c.execute(
            """
            SELECT id, buyPrice, num
            FROM stock
            WHERE stockname = ? AND userid = ?""",
            (self.symbol, self.userid))
        available_stock = c.fetchall()
        if available_stock == []:
            print("You do not have this stock")
        else:
            stock_id, price, on_hand = available_stock
        if self.quantity > on_hand:
            print("Not enough stock available!")
            return

        c.execute(
            """
            UPDATE stock
            SET num = num - ?
            WHERE id = ?""",
            (self.quanity, stock_id))
        connection.commit()

        revenue = price * self.quantity
        print("Stock sell sucessesful."
              "You have gained {}".format(revenue))

        c.execute(
            """
            UPDATE users
            SET balance = balance + ?
            WHERE id = ?""",
            (revenue, self.userid))
        connection.commit()
        return revenue

    def get_portfolio(self, name, username):
        "first fine user id from his name and username, then use this id to find all the stocks he has"
        portfolio = []
        c.execute("""
            SELECT * FROM stock where userid =(SELECT id FROM user WHERE name = ? AND username = ?)"""), (name, username)
        return portfolio.fetchall() 
        connection.commit()

    def admin_view(self, userid, acttype, balance):
        "Need to select all stocks from all users, ordered by user name"
        pass
