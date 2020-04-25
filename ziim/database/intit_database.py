import sqlite3

from sqlite3 import Error

from admin.model import *

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

# dataBase = './database/ziim.db'

# Admin_Table = 'admin'
# Meeting_Table = 'meeting'
# Code_Table = 'code'
# Page_Content_Table = 'page_content'


# Admin_Columns = ['id','email','password','payment']
# Meeting_Columns = ['id', 'admin_id', 'start_at', 'name', 
#                     'zoom_meeting_id', 'zoom_meeting_password', 
#                     'ticket_count', 'price', 'page_url']
# Code_Columns = ['id', 'event_id', 'is_used']
# Page_Content_Columns = ['id', 'meeting_id', 'admin_id']

con = sql_connection(dataBase)

sql_table(con, Admin_Table,'(id int, email varchar, password password, payment varchar)')
sql_table(con, Meeting_Table,'(id int, admin_id int, start_at timestamp, name varchar, zoom_meeting_id varchar, zoom_meeting_password varchar, ticket_count int, price double, page_url varchar)')
sql_table(con, Code_Table,'(id int PRIMARY KEY, event_id int, is_used boolean)')
sql_table(con, Page_Content_Table,'(id int PRIMARY KEY, meeting_id int, admin_id int)')

entities = (1, 'first_admin@gmail.com', 'password', '911')
sql_insert(con,Admin_Table, entities)

entities = (1, 1, None, 'Math', None, None, 50, 50000, 'page url Math')
sql_insert(con,Meeting_Table, entities)
entities = (2, 1, None, 'Math 2', None, None, 50, 55000, 'page url Math 2')
sql_insert(con,Meeting_Table, entities)

con.close()
