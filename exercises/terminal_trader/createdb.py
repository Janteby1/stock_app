
import sqlite3

connection = sqlite3.connect('stocks.db')
cursor = connection.cursor()

connection.execute(
    """
    DROP TABLE IF EXISTS users;
    """
)
connection.execute(
    """
    DROP TABLE IF EXISTS stocks;
    """
)

connection.execute(
    """
    CREATE TABLE users (
        id INTEGER PRIMARY KEY, 
        name TEXT, 
        username TEXT, 
        password TEXT,
        balance INTEGER
    )
    """
)

connection.execute(
    """
    CREATE TABLE stock (
        id INTEGER PRIMARY KEY, 
        stockName TEXT, 
        buyPrice INTEGER, 
        num INTEGER,
        userid INTEGER,
        FOREIGN KEY(userid) REFERENCES users(id)
    )
    """
)

connection.commit()

print ("Database created")
connection.close()
