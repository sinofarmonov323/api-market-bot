import sqlite3

def create_api_table():
    with sqlite3.connect("database.db") as con:
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS apis (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, url TEXT, callback_name TEXT, caption TEXT, price TEXT, UNIQUE(name, url, callback_name))")
        con.commit()

create_api_table()

def create_users_table():
    with sqlite3.connect("database.db") as con:
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, username TEXT, UNIQUE(user_id, username))")
        con.commit()

create_users_table()

def add_user(user_id, username):
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)", (user_id, username,))

def add_api(name: str, url: str, callback_name: str, caption: str, price: str):
    with sqlite3.connect("database.db") as con:
        cursor = con.cursor()
        cursor.execute("INSERT OR IGNORE INTO apis (name, url, callback_name, caption, price) VALUES (?, ?, ?, ?, ?)", (name,url,callback_name,caption,price,))
        con.commit()

def get_callback_names() -> list:
    with sqlite3.connect("database.db") as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT callback_name FROM apis")
        rows = cur.fetchall()
        return [row["callback_name"] for row in rows]

def update_api_by_callback_name(name: str, new_name: str, url: str, callback_name: str, caption: str, price: str):
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("UPDATE apis SET name = ?, url = ?, callback_name = ?, caption = ?, price = ? WHERE name = ?", (new_name, url, callback_name, caption, price, name))

def get_api(callback_name: str):
    with sqlite3.connect("database.db") as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM apis WHERE callback_name = ?", (callback_name,))
        return dict(cur.fetchone())

def get_all_apis():    
    with sqlite3.connect("database.db") as con:
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        cursor.execute("SELECT * FROM apis")
        datas = cursor.fetchall()
        return [dict(data) for data in datas]

def delete_api(name: str):
    with sqlite3.connect("database.db") as con:
        cursor = con.cursor()
        cursor.execute("DELETE FROM apis WHERE name IN (?)", (name,))
        con.commit()

def get_all_users_number():
    with sqlite3.connect("database.db") as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM users")
        data = cur.fetchall()
        return [dict(row)['user_id'] for row in data]
