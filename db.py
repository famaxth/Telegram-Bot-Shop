# - *- coding: utf- 8 - *-

#Production by Famaxth
#Telegram - @famaxth


import sqlite3

def ensure_connection(func):

    def decorator(*args, **kwargs):
        with sqlite3.connect('anketi.db') as conn:
            result = func(conn, *args, **kwargs)

        return result

    return decorator


@ensure_connection
def init_db(conn, force: bool = False):

    c = conn.cursor()

    if force:
        c.execute("DROP TABLE IF EXISTS users")

    c.execute("""CREATE TABLE IF NOT EXISTS users (
        id              INTEGER PRIMARY KEY,
        first_name                   STRING,
        last_name                    STRING,
        date                         STRING,
        user_id                     INTEGER,
        balance           INTEGER DEFAULT 0,
        take_money        INTEGER DEFAULT 0,
        purchase          INTEGER DEFAULT 0,
        lang        STRING DEFAULT Russian);
    """)

    c.execute('''CREATE TABLE IF NOT EXISTS position (
        id              INTEGER PRIMARY KEY,
        lot               INTEGER DEFAULT 0,
        name_katalog                 STRING,
        name                         STRING,
        description                  STRING,
        price                       INTEGER,
        item                        STRING);
    ''')

    c.execute('''CREATE TABLE IF NOT EXISTS product(
        id              INTEGER PRIMARY KEY,
        url                          STRING,
        name                        STRING);
    ''')

    c.execute('''CREATE TABLE IF NOT EXISTS buyers(
        id                  INTEGER PRIMARY KEY,
        first_name                       STRING,
        last_name                       STRING);
    ''')

    c.execute('''CREATE TABLE IF NOT EXISTS cash(
        id                   INTEGER PRIMARY KEY,
        cash                  INTEGER DEFAULT 0);
    ''')

    c.execute('''CREATE TABLE IF NOT EXISTS katalog(
        id                  INTEGER PRIMARY KEY,
        name                             STRING,
        description                     STRING);
    ''')

    c.execute('''CREATE TABLE IF NOT EXISTS sales(
        id                  INTEGER PRIMARY KEY,
        user_id                         INTEGER,                            
        price                           INTEGER,
        date                            STRING);
    ''')

    c.execute('''CREATE TABLE IF NOT EXISTS qiwi(
        id                  INTEGER PRIMARY KEY,
        later                 INTEGER DEFAULT 0,
        now                  INTEGER DEFAULT 0);
    ''')

    c.execute('''CREATE TABLE IF NOT EXISTS settings(
        id                        NTEGER PRIMARY KEY,
        information              STRING DEFAULT text,
        hello                    STRING DEFAULT text,
        contact                  STRING DEFAULT text,
        payment                 STRING DEFAULT text);
    ''')

    conn.commit()




@ensure_connection
def edit_settings_inf(conn, information: str):
    c = conn.cursor()

    c.execute('UPDATE settings SET information = ?', (information,))

    conn.commit()


@ensure_connection
def edit_settings_con(conn, contact: str):
    c = conn.cursor()

    c.execute('UPDATE settings SET contact = ?', (contact,))

    conn.commit()


@ensure_connection
def edit_settings_hel(conn, hello: str):
    c = conn.cursor()

    c.execute('UPDATE settings SET hello = ?', (hello,))

    conn.commit()


@ensure_connection
def edit_settings_pay(conn, payment: str):
    c = conn.cursor()

    c.execute('UPDATE settings SET payment = ?', (payment,))

    conn.commit()


@ensure_connection
def add_product(conn, url: str, name: str):
    c = conn.cursor()

    c.execute("INSERT INTO product (url, name) VALUES (?, ?)", (url, name))

    conn.commit()


@ensure_connection
def add_user(conn, first_name: str, last_name: str, date: str, user_id):
    c = conn.cursor()

    c.execute("INSERT INTO users (first_name, last_name, date, user_id) VALUES (?, ?, ?, ?)", (first_name, last_name, date, user_id))

    conn.commit()


@ensure_connection
def add_position(conn, name_katalog: str, name: str, description: str, price, item: str, lot):
    c = conn.cursor()

    c.execute("INSERT INTO position (name_katalog, name, description, price, item, lot) VALUES (?, ?, ?, ?, ?, ?)", (name_katalog, name, description, price, item, lot))

    conn.commit()


@ensure_connection
def add_katalog(conn, name: str, description: str):
    c = conn.cursor()

    c.execute("INSERT INTO katalog (name, description) VALUES (?, ?)", (name, description))

    conn.commit()


@ensure_connection
def delete_katalog(conn, name):
    c = conn.cursor()

    c.execute('DELETE FROM katalog WHERE name = ?', (name,))

    conn.commit()


@ensure_connection
def delete_position(conn, name):
    c = conn.cursor()

    c.execute('DELETE FROM position WHERE name = ?', (name,))

    conn.commit()


@ensure_connection
def edit_position(conn, description: str, name: str):
    c = conn.cursor()

    c.execute('UPDATE position SET description = ? WHERE name = ?', (description, name,))

    conn.commit()


@ensure_connection
def change_position(conn, price: str, name: str):
    c = conn.cursor()

    c.execute('UPDATE position SET price = ? WHERE name = ?', (price, name,))

    conn.commit()


@ensure_connection
def add_take_money(conn, take_money, user_id):
    c = conn.cursor()

    c.execute('UPDATE users SET take_money = ? WHERE user_id = ?', (take_money, user_id,))

    conn.commit()


@ensure_connection
def add_balance(conn, balance, user_id):
    c = conn.cursor()

    c.execute('UPDATE users SET balance = ? WHERE user_id = ?', (balance, user_id,))

    conn.commit()


@ensure_connection
def add_qiwi_later(conn, later):
    c = conn.cursor()

    c.execute('UPDATE qiwi SET later = ? WHERE id = 1', (later,))

    conn.commit()


@ensure_connection
def update_user_balance(conn, balance, user_id):
    c = conn.cursor()

    c.execute('UPDATE users SET balance = ? WHERE user_id = ?', (balance, user_id,))

    conn.commit()


@ensure_connection
def update_user_purchase(conn, purchase, user_id):
    c = conn.cursor()

    c.execute('UPDATE users SET purchase = ? WHERE user_id = ?', (purchase, user_id,))

    conn.commit()


@ensure_connection
def add_qiwi_now(conn, now):
    c = conn.cursor()

    c.execute('UPDATE qiwi SET now = ? WHERE id = 1', (now,))

    conn.commit()


@ensure_connection
def return_katalog(conn):
    c = conn.cursor()

    c.execute("SELECT name FROM katalog")

    all_results = c.fetchall()

    return all_results


@ensure_connection
def return_hello(conn):
    c = conn.cursor()

    c.execute("SELECT hello FROM settings")

    all_results = c.fetchone()

    return all_results


@ensure_connection
def return_contact(conn):
    c = conn.cursor()

    c.execute("SELECT contact FROM settings")

    all_results = c.fetchone()

    return all_results


@ensure_connection
def return_information(conn):
    c = conn.cursor()

    c.execute("SELECT information FROM settings")

    all_results = c.fetchone()

    return all_results


@ensure_connection
def return_payment(conn):
    c = conn.cursor()

    c.execute("SELECT payment FROM settings")

    all_results = c.fetchone()

    return all_results


@ensure_connection
def return_qiwi_later(conn):
    c = conn.cursor()

    c.execute("SELECT later FROM qiwi")

    all_results = c.fetchone()

    return all_results


@ensure_connection
def return_qiwi_now(conn):
    c = conn.cursor()

    c.execute("SELECT now FROM qiwi")

    all_results = c.fetchone()

    return all_results


@ensure_connection
def return_tovar_description(conn, name):
    c = conn.cursor()

    c.execute("SELECT description FROM position WHERE name = ?", (name,))

    all_results = c.fetchone()

    return all_results


@ensure_connection
def return_tovar_price(conn, name):
    c = conn.cursor()

    c.execute("SELECT price FROM position WHERE name = ?", (name,))

    all_results = c.fetchone()

    return all_results


@ensure_connection
def return_tovar_lot(conn, name):
    c = conn.cursor()

    c.execute("SELECT lot FROM position WHERE name = ?", (name,))

    all_results = c.fetchone()

    return all_results


@ensure_connection
def show_user_name(conn, user_id):
    c = conn.cursor()

    c.execute("SELECT first_name FROM users WHERE user_id = ?", (user_id,))

    all_results = c.fetchone()

    return all_results


@ensure_connection
def show_user_register(conn, user_id):
    c = conn.cursor()

    c.execute("SELECT date FROM users WHERE user_id = ?", (user_id,))

    all_results = c.fetchone()

    return all_results


@ensure_connection
def show_user_purchase(conn, user_id):
    c = conn.cursor()

    c.execute("SELECT purchase FROM users WHERE user_id = ?", (user_id,))

    all_results = c.fetchone()

    return all_results


@ensure_connection
def show_user_sale(conn, user_id):
    c = conn.cursor()

    c.execute("SELECT item FROM sales WHERE user_id = ?", (user_id,))

    all_results = c.fetchall()

    return all_results


@ensure_connection
def show_user_balance(conn, user_id):
    c = conn.cursor()

    c.execute("SELECT balance FROM users WHERE user_id = ?", (user_id,))

    all_results = c.fetchone()

    return all_results


@ensure_connection
def show_user_take_money(conn, user_id):
    c = conn.cursor()

    c.execute("SELECT take_money FROM users WHERE user_id = ?", (user_id,))

    all_results = c.fetchone()

    return all_results


@ensure_connection
def find_user_balance_name(conn, user_id):
    c = conn.cursor()

    c.execute("SELECT balance, first_name FROM users WHERE user_id = ?", (user_id,))

    all_results = c.fetchone()

    return all_results


@ensure_connection
def find_user_purchase_name(conn, user_id):
    c = conn.cursor()

    c.execute("SELECT purchase, first_name FROM users WHERE user_id = ?", (user_id,))

    all_results = c.fetchone()

    return all_results


@ensure_connection
def return_users(conn):
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM users")

    all_results = c.fetchone()

    return all_results


@ensure_connection
def return_users_2(conn):
    c = conn.cursor()

    c.execute("SELECT first_name, date, user_id FROM users")

    all_results = c.fetchall()

    return all_results


@ensure_connection
def return_buyers(conn):
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM buyers")

    all_results = c.fetchone()

    if all_results == None:
        x = [0]
        return x
    else:
        return all_results


@ensure_connection
def return_buyers_2(conn):
    c = conn.cursor()

    c.execute("SELECT id FROM buyers")

    all_results = c.fetchall()

    return all_results


@ensure_connection
def return_position(conn):
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM position")

    all_results = c.fetchone()

    if all_results == None:
        x = [0]
        return x
    else:
        return all_results


@ensure_connection
def return_katalog_2(conn):
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM katalog")

    all_results = c.fetchone()

    return all_results


@ensure_connection
def return_position_2(conn):
    c = conn.cursor()

    c.execute("SELECT * FROM position")

    all_results = c.fetchall()

    return all_results


@ensure_connection
def return_position_3(conn):
    c = conn.cursor()

    c.execute("SELECT name FROM position")

    all_results = c.fetchall()

    return all_results


@ensure_connection
def return_position_price(conn):
    c = conn.cursor()

    c.execute("SELECT price FROM position")

    all_results = c.fetchall()

    return all_results


@ensure_connection
def return_product_4(conn):
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM product")

    all_results = c.fetchone()

    if all_results == None:
        x = [0]
        return x
    else:
        return all_results


@ensure_connection
def return_position_4(conn, name_katalog):
    c = conn.cursor()

    c.execute("SELECT name FROM position WHERE name_katalog = ?", (name_katalog,))

    all_results = c.fetchall()

    return all_results


@ensure_connection
def defcon(conn, name):
    c = conn.cursor()

    c.execute("SELECT description FROM katalog WHERE name = ?", (name,))

    all_results = c.fetchone()

    return all_results


@ensure_connection
def return_position_5(conn, name_katalog):
    c = conn.cursor()

    c.execute("SELECT COUNT(name_katalog) FROM position WHERE name_katalog = ?", (name_katalog,))

    all_results = c.fetchall()

    return all_results


@ensure_connection
def name_pos(conn):
    c = conn.cursor()

    c.execute("SELECT name_katalog FROM position")

    all_results = c.fetchall()

    return all_results


@ensure_connection
def name_kat(conn):
    c = conn.cursor()

    c.execute("SELECT name FROM katalog")

    all_results = c.fetchall()

    return all_results


@ensure_connection
def return_product_2(conn):
    c = conn.cursor()

    c.execute("SELECT name FROM product")

    all_results = c.fetchall()

    return all_results


@ensure_connection
def return_product_3(conn):
    c = conn.cursor()

    c.execute("SELECT * FROM product")

    all_results = c.fetchall()

    return all_results


@ensure_connection
def return_sales(conn):
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM sales")

    all_results = c.fetchone()

    if all_results == None:
        x = [0]
        return x
    else:
        return all_results


@ensure_connection
def return_cash(conn):
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM cash")

    all_results = c.fetchone()

    return all_results


@ensure_connection
def return_product(conn):
    c = conn.cursor()

    c.execute("SELECT name FROM product")

    all_results = c.fetchone()

    return all_results


@ensure_connection
def return_lot(conn, price):
    c = conn.cursor()

    c.execute("SELECT lot FROM position WHERE price = ?", (price,))

    all_results = c.fetchone()

    return all_results


@ensure_connection
def return_position_item(conn, price):
    c = conn.cursor()

    c.execute("SELECT item FROM position WHERE price = ?", (price,))

    all_results = c.fetchone()

    return all_results


@ensure_connection
def return_user_lang(conn, user_id):
    c = conn.cursor()

    c.execute("SELECT lang FROM users WHERE user_id = ?", (user_id,))

    all_results = c.fetchone()

    return all_results


@ensure_connection
def return_item(conn, name):
    c = conn.cursor()

    c.execute("SELECT url FROM product WHERE name = ?", (name,))

    all_results = c.fetchone()

    return all_results


@ensure_connection
def return_purchase(conn, user_id):
    c = conn.cursor()

    c.execute("SELECT purchase FROM users WHERE user_id = ?", (user_id,))

    all_results = c.fetchone()

    return all_results


@ensure_connection
def edit_lot(conn, lot, price):
    c = conn.cursor()

    c.execute('UPDATE position SET lot = ? WHERE price = ?', (lot, price,))

    conn.commit()


@ensure_connection
def update_user_lang(conn, lang, user_id):
    c = conn.cursor()

    c.execute('UPDATE users SET lang = ? WHERE user_id = ?', (lang, user_id,))

    conn.commit()


@ensure_connection
def add_purchase(conn, purchase, user_id):
    c = conn.cursor()

    c.execute('UPDATE users SET purchase = ? WHERE user_id = ?', (purchase, user_id,))

    conn.commit()


@ensure_connection
def edit_cash(conn, cash):
    c = conn.cursor()

    c.execute('UPDATE cash SET cash = ?', (cash,))

    conn.commit()


@ensure_connection
def add_buyer(conn, id, first_name: str, last_name: str):
    c = conn.cursor()

    c.execute("INSERT INTO buyers (id, first_name, last_name) VALUES (?, ?, ?)", (id, first_name, last_name))

    conn.commit()


@ensure_connection
def add_sale(conn, user_id, price, date: str):
    c = conn.cursor()

    c.execute("INSERT INTO sales (user_id, price, date) VALUES (?, ?, ?)", (user_id, price, date))

    conn.commit()


@ensure_connection
def return_cash_1(conn):
    c = conn.cursor()

    c.execute("SELECT cash FROM cash")

    all_results = c.fetchone()

    if all_results == None:
        x = 0
        return x
    else:
        return all_results


@ensure_connection
def return_cash_100(conn):
    c = conn.cursor()

    c.execute("SELECT cash FROM cash")

    all_results = c.fetchone()

    if all_results == None:
        x = (0,)
        return x
    else:
        return all_results
