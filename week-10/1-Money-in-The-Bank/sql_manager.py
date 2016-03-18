import sqlite3
from client import Client
import string
import helpers
import settings

conn = sqlite3.connect(settings.DB_NAME)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

def initialize_database():
    pass

def check_password_strength(password, username):
    if len(password) > settings.MIN_PWD_LENGTH:
        has_number = False
        has_spec_symbol = False
        has_capital = False
        special_symbols = string.punctuation
        numbers = "1234567890"
        for ch in password:   # check for capital letters
            if ch in special_symbols:
                has_spec_symbol = True
            if ch in numbers:
                has_number = True
            if ord(ch) >= 65 and ord(ch) <= 90:
                has_capital = True
            if has_spec_symbol and has_number and has_capital:
                return username not in password
    return False


def create_clients_table():
    create_query = '''CREATE TABLE IF NOT EXISTS
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                salt TEXT)'''

    cursor.execute(create_query)


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = ? WHERE id = ?;"
    cursor.execute(update_sql, (new_message, logged_user.get_id(),))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    update_sql = "UPDATE clients SET password = ? WHERE id = ?"
    cursor.execute(update_sql, (new_pass, logged_user.get_id()))
    conn.commit()


def register(username, password):
    if check_password_strength(password, username):
        insert_sql = "insert into clients (username, password, salt) values (?, ?, ?);"
        hash_salt_pair = helpers.hash_password_salt_tuple(password)
        cursor.execute(insert_sql, (username, hash_salt_pair[0],
                       hash_salt_pair[1]))
        conn.commit()
        print ("OK")
        return True
        # password not strong enough, better throw an excpetion
    else:
        return False


def get_user_salt(username):
    sql = ''' SELECT salt
              FROM clients
              WHERE username = ?;
    '''
    cursor.execute(sql, (username, ))

    conn.commit()
    salt = cursor.fetchone()
    return salt[0]


def login(username, password):
    select_query = """SELECT id, username, balance, message
                      FROM clients
                      WHERE username = ?
                      AND password = ?
                      LIMIT 1;"""
    salt = get_user_salt(username)
    hashed_password = helpers.hash_password_salt_tuple(password, salt)[0]
    cursor.execute(select_query, (username, hashed_password))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    return False
