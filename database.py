import pandas as pd
import sqlite3

conn = sqlite3.connect('hotel_conn.db')

conn.execute("""CREATE TABLE IF NOT EXISTS HOTEL_INFO (CITY TEXT NOT NULL, RESTAURANTS TEXT NOT NULL, FOOD_ITEM TEXT NOT NULL, PRICE TEXT NOT NULL);""")

conn.execute('INSERT INTO HOTEL_INFO (CITY, RESTAURANTS, FOOD_ITEM, PRICE) VALUES ("BANGALORE", "EAT.FIT", "Pindi Chole Paratha Thali", "170")')
conn.execute('INSERT INTO HOTEL_INFO (CITY, RESTAURANTS, FOOD_ITEM, PRICE) VALUES ("BANGALORE", "EAT.FIT", "Murg Khurchan", "284")')
conn.execute('INSERT INTO HOTEL_INFO (CITY, RESTAURANTS, FOOD_ITEM, PRICE) VALUES ("BANGALORE", "NANDHINI DELUX", "Nandhini Special Carrier Meals", "375")')
conn.execute('INSERT INTO HOTEL_INFO (CITY, RESTAURANTS, FOOD_ITEM, PRICE) VALUES ("MUMBAI", "Theobroma", "Fresh Cream Pineapple Pastry", "130")')
conn.execute('INSERT INTO HOTEL_INFO (CITY, RESTAURANTS, FOOD_ITEM, PRICE) VALUES ("MUMBAI", "Guru Kripa", "Sev Barfi", "180")')
conn.execute('INSERT INTO HOTEL_INFO (CITY, RESTAURANTS, FOOD_ITEM, PRICE) VALUES ("MUMBAI", "Guru Kripa", "Sweet Lassi", "60")')
conn.execute('INSERT INTO HOTEL_INFO (CITY, RESTAURANTS, FOOD_ITEM, PRICE) VALUES ("MUMBAI", "Guru Kripa", "Roti Bhaji Thali", "140")')
conn.execute('INSERT INTO HOTEL_INFO (CITY, RESTAURANTS, FOOD_ITEM, PRICE) VALUES ("MUMBAI", "Cafe Safar", "Boneless Butter Chicken", "190")')
conn.execute('INSERT INTO HOTEL_INFO (CITY, RESTAURANTS, FOOD_ITEM, PRICE) VALUES ("MUMBAI", "Cafe Safar", "Chicken Crispy", "220")')
conn.execute('INSERT INTO HOTEL_INFO (CITY, RESTAURANTS, FOOD_ITEM, PRICE) VALUES ("PUNE", "Le Plaisir", "Blueberry Cheesecake", "285.71")')
conn.execute('INSERT INTO HOTEL_INFO (CITY, RESTAURANTS, FOOD_ITEM, PRICE) VALUES ("PUNE", "Le Plaisir", "Espresso Pannacotta", "285.71")')
conn.commit()
conn.close()

conn = sqlite3.connect('hotel_conn.db')
all =  conn.execute("SELECT * FROM HOTEL_INFO")
print("HERE", all)

for i in all:
    print("HEREHERE")
    print(i)
# conn.execute("")
