import sqlite3
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
    def end(self):
        self.con.close()
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
    def get_id_pass(self, meeting_id):
        rows = self.sql_fetch('SELECT * FROM "'+Meeting_Table + '" WHERE '+ Meeting_Columns[0] + ' = "' + str(meeting_id) + '"')
        if len(rows) == 0:
            print('no match meeting')
            return None, None
        return rows[0][4], rows[0][5]
    
