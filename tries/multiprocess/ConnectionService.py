
def connectPostgres():
    import psycopg2
    try:
        # Connect to the database
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            user="postgres",
            password="admin",
            database="bildiri"
        )
    except psycopg2.Error as e:
        print("Error connecting to the database:")
        print(e)
    else:
        #print("Connection established successfully")
        return conn,conn.cursor()
    

def connectSqlite():
    import sqlite3
    conn = sqlite3.connect('bildiri.sqlite')
    cur = conn.cursor()
    createSqliteTables(cur,conn)
    return conn,conn.cursor()


def createSqliteTables(cur,conn):
    cur.execute("CREATE TABLE IF NOT EXISTS agent( id INTEGER PRIMARY KEY AUTOINCREMENT, state text);")
    cur.execute("CREATE TABLE IF NOT EXISTS offer( id INTEGER PRIMARY KEY AUTOINCREMENT,aid integer, price INTEGER, FOREIGN KEY(aid) REFERENCES agent(id) );")
    conn.commit()


connectSqlite()


