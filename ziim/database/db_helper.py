import sqlite3
import traceback
import sys

def insert(statement):
    try:
        sqliteConnection = sqlite3.connect('ziim.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
    
        sqlite_insert_query = statement
    
        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        cursor.close()
        return True

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table")
        print(error)
        return False

    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")


def is_exists(statement):
    try:
        sqliteConnection = sqlite3.connect('ziim.db', timeout=20)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = statement
        cursor.execute(sqlite_select_query)
        totalRows = cursor.fetchone()[0]
        cursor.close()

        return totalRows > 0
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
        return False
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The Sqlite connection is closed")