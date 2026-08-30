import sqlite3
con = sqlite3.connect("economy.db")
con.execute("CREATE TABLE IF NOT EXISTS users(user_id PRIMARY KEY, username, balance INTEGER DEFAULT 1000, last_daily DEFAULT 0, last_rob DEFAULT 0)")
con.commit()

def add_user(user_id, username):
    con.execute(""" INSERT OR IGNORE INTO users (user_id, username)VALUES (?,?)""",(user_id,username))
    con.commit()

def get_balance(user_id):
    cur = con.execute("""SELECT balance FROM users WHERE user_id = ?""",(user_id,))
    result = cur.fetchone()
    return result[0]

def update_balance(user_id, amount):
    cur = con.execute("""UPDATE users SET balance = balance + ? WHERE user_id = ?""",(amount, user_id))
    con.commit()

def set_last_daily(user_id, timestamp):
    con.execute("""UPDATE users SET last_daily = ? WHERE user_id = ?""",(timestamp,user_id))
    con.commit()

def set_last_rob(user_id, timestamp):
    con.execute("""UPDATE users SET last_rob = ? WHERE user_id = ?""",(timestamp, user_id))
    con.commit()

def get_last_daily(user_id):
    cur = con.execute("""SELECT last_daily FROM users WHERE user_id = ?""",(user_id))
    result = cur.fetchone()
    return result[0]

def get_last_rob(user_id):
    cur = con.execute("""SELECT last_rob FROM users WHERE user_id = ?""",(user_id))
    result = cur.fetchone()
    return result[0]

def get_top_users():
    cur = con.execute("""SELECT username, balance FROM users ORDER BY balance DESC LIMIT 5""")
    return cur.fetchall()
