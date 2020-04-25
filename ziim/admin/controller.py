import sqlite3
from admin.model import *
from database.sqlite import SQLite_id_pass
from sqlite3 import Error
import os

if os.path.isfile(dataBase):
    print ("File exist")
else:
    print ("File not exist")
ob = SQLite_id_pass(dataBase)

# print(ob.sql_list_table())

def update_zoom_meeting(admin_email, meeting_id, zoom_meeting_id, zoom_meeting_password):
    return (ob.update_id_pass(admin_email, meeting_id, zoom_meeting_id, zoom_meeting_password))


# print(ob.sql_fetch('SELECT * FROM "'+Meeting_Table + '"'))
def update_zoom_meeting(admin_email, meeting_id):
    return  (ob.get_id_pass(admin_email, meeting_id))