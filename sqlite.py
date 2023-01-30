import sqlite3

con = sqlite3.connect('coffee.sqlite')
cur = con.cursor()

cur.execute('''CREATE TABLE coffee(
    id INT PRIMARY KEY NOT NULL,
    sort_name TEXT,
    roast_degree INT,
    ground__in_grains TEXT,
    taste_description TEXT,
    price INT,
    packing_volume INT
)''')

cur.execute('''INSERT INTO coffee(id, sort_name, roast_degree, ground__in_grains, taste_description, price, packing_volume) VALUES
    (1, "арабика", 50, "молотый", "вкусный", 228, 1337)
''')

con.commit()
con.close()
