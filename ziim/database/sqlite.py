import sqlite3

<<<<<<< HEAD
from admin.model import *

from sqlite3 import Error

class SQLite:
    def __init__(self, dataBase):
        self.con = self.sql_connection(dataBase)
    def sql_connection(self, dataBase):
        try:
            con = sqlite3.connect(dataBase)
            return con
        except Error:
            print(Error)
    def sql_insert(self, tableName, entities):
        cursorObj = self.con.cursor()
        # cursorObj.execute('INSERT INTO '+tableName+ ' ' +columns+' VALUES(?' + ', ?'*(len(entities)-1) +')', entities)
        cursorObj.execute('INSERT INTO '+tableName+' VALUES(?' + ', ?'*(len(entities)-1) +')', entities)
        self.con.commit()
    def sql_update(self, query):
        cursorObj = self.con.cursor()
        cursorObj.execute(query)
        self.con.commit()
    def sql_fetch(self, query):
        cursorObj = self.con.cursor()
        cursorObj.execute(query)
        rows = cursorObj.fetchall()
        return rows
    def sql_list_table(self):
        cursorObj = self.con.cursor()
        cursorObj.execute('SELECT name from sqlite_master where type= "table"')
        return (cursorObj.fetchall())


class SQLite_id_pass(SQLite):
    def __init__(self, dataBase):
        self.con = self.sql_connection(dataBase)

    def update_id_pass(self, admin_email, meeting_id, zoom_meeting_id, zoom_meeting_password):
        rows = self.sql_fetch('SELECT * FROM "'+Admin_Table + '" WHERE '+Admin_Columns[1] + ' = "' + admin_email + '"')
        if len(rows) == 0:
            print('no match admin')
            return False
        admin_id = rows[0][0]
        print('admin_id: ', admin_id)
        rows = self.sql_fetch('SELECT * FROM "'+Meeting_Table + '" WHERE '+Meeting_Columns[1] + ' = ' + str(admin_id) + ' AND ' + Meeting_Columns[0] + ' = ' + str(meeting_id) + '')
        if len(rows) == 0:
            print('no match meeting')
            return False
        print('update\n')
        self.sql_update('UPDATE "'+Meeting_Table + '" SET '+Meeting_Columns[4] + ' = "' + zoom_meeting_id + '", '+Meeting_Columns[5] + ' = "' + zoom_meeting_password + '" WHERE ' + Meeting_Columns[0] + ' = ' + str(meeting_id) + '')
        return True
    def get_id_pass(self, admin_email, meeting_id):
        rows = self.sql_fetch('SELECT * FROM "'+Admin_Table + '" WHERE '+Admin_Columns[1] + ' = "' + admin_email + '"')
        if len(rows) == 0:
            print('no match admin')
            return None, None
        admin_id = rows[0][0]
        rows = self.sql_fetch('SELECT * FROM "'+Meeting_Table + '" WHERE '+Meeting_Columns[1] + ' = "' + str(admin_id) + '" AND ' + Meeting_Columns[0] + ' = "' + str(meeting_id) + '"')
        if len(rows) == 0:
            print('no match meeting')
            return None, None
        return rows[0][4], rows[0][5]
    
=======
from sqlite3 import Error

def sql_connection(dataBase):
    try:
        con = sqlite3.connect(dataBase)
        return con
    except Error:
        print(Error)
def sql_table(con, tableName, content):
    cursorObj = con.cursor()
    cursorObj.execute('drop table if exists ' + tableName)
    cursorObj.execute('create table if not exists '+tableName+content)
    con.commit()
def sql_insert(con, tableName, entities):
    cursorObj = con.cursor()
    # cursorObj.execute('INSERT INTO '+tableName+ ' ' +columns+' VALUES(?' + ', ?'*(len(entities)-1) +')', entities)
    cursorObj.execute('INSERT INTO '+tableName+' VALUES(?' + ', ?'*(len(entities)-1) +')', entities)
    con.commit()

def sql_fetch(con, tableName):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM '+tableName+'')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

dataBase = 'ziim.db'
Admin_user_Table = 'admin_user'
Room_Table = 'room'
Room_activate_Table = 'room_activate'

con = sql_connection(dataBase)
Admin_user_Columns = ['email','name','payment']
Room_Columns = ['room', 'admin_email']
Room_activate_Columns = ['room', 'meeting_id', 'pass']
User_Columns  = ['email', 'room']

sql_table(con, Admin_user_Table,'(email text PRIMARY KEY, name text, payment text)')
sql_table(con, Room_Table,'(room text PRIMARY KEY, admin text)')
sql_table(con, Room_activate_Table,'(room text PRIMARY KEY, meeting_id text, pass text)')

entities = ('test@gmail.com', 'God', '113')
sql_insert(con,Admin_user_Table, entities)

entities = ('Math', 'test@gmail.com')
sql_insert(con,Room_Table, entities)
entities = ('Math 2', 'test@gmail.com')
sql_insert(con,Room_Table, entities)

con.close()
>>>>>>> 61d4a74a48bebfeba87f91e5fde4b12d365866e8
