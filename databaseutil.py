
import pymysql

conn = None
def get_connection():
    global conn
    if conn==None:
        conn = pymysql.connect('localhost', 'root', 'chiu', 'pydb1')
        # return conn
    else:
        return conn


def generic_way():
    conn = get_connection()
    channel = conn.cursor()
    # conn.commit()
    return channel
