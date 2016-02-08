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
        return(stock_info)

    def create_user(self, name, username, password, balance):
        c.execute("""
            INSERT INTO users ("name", "username", "password", "balance") VALUES (?, ?, ?, ?)""",(name, username, password, balance))
        connection.commit()

    def print_user(self):
        cursor = connection.execute("SELECT name, username, password, permission FROM users")
        i = 0
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

        info_list = self.stock_info(symbol)

        self.lastprice=info_list["LastPrice"]
        print('buy Price  ',self.lastprice, '  ','user id ..',userid )

        total_price_of_shares = int(num) * int(self.lastprice)

        c.execute("""
            INSERT INTO stock ("stockName","buyPrice","num","userid") VALUES(?,?,?,?)
        
        """,(symbol,self.lastprice,num,userid)
        )

        c.execute("""
            UPDATE users SET balance=balance - ? WHERE id=?""",(total_price_of_shares, userid)
        )
        print ("Your purchase has gone through")

        connection.commit()
    
    def sell_stock(self, symbol,quantity,userid):
        self.symbol = symbol
        self.quantity = quantity
        self.userid = userid
        print('SYMBOL  ',self.symbol)

        info_list = self.stock_info(self.symbol)
        # print('self stok info  --',self.stock_info(self.symbol))
        # print('IN MODEL SELL STOCK..',info_list)
        self.lastprice = info_list["LastPrice"]
        print('Sell price', self.lastprice, ' ', 'user id..', self.userid )
        total_revenue = int(self.quantity) * int(self.lastprice)

        c.execute(
            """
            SELECT id, buyPrice, num
            FROM stock
            WHERE stockname = ? AND userid = ?""",
            (self.symbol, self.userid))
        available_stock = c.fetchall()
        print('available stock.....',available_stock)
        if available_stock == []:
            print("You do not have this stock")
        else:
            stock_id = available_stock[0][0]
            price = available_stock[0][1]
            on_hand = available_stock[0][2]
            
        if int(self.quantity) > int(on_hand):
            print("Not enough stock available!")
            return

        c.execute(
            """
            UPDATE stock
            SET num = num - ?
            WHERE id = ?""",
            (self.quantity, stock_id))
        connection.commit()

        revenue = int(price) * int(self.quantity)
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

    def get_portfolio(self, username, password):
        "first fine user id from his name and username, then use this id to find all the stocks he has"
        portfolio = []
        userid = c.execute("""
            SELECT id 
                FROM users 
                WHERE username = ? AND password = ? 
                """,
                (username, password))
        userid = userid.fetchone()

        portfolio = c.execute("""
            SELECT stockName, buyPrice, num, userid
                FROM stock
                WHERE userid = ?
                """,
                (userid))
        connection.commit()

        return portfolio.fetchall()

    def get_top_accounts(self):
        """
        Retrieve top accounts from database.
        """
        c.execute(
        """
        SELECT name, balance
        FROM users
        WHERE name != "admin"
        ORDER BY balance DESC
        """)
        return c.fetchall()
