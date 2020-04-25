dataBase = './database/ziim.db'

Admin_Table = 'admin'
Meeting_Table = 'meeting'
Code_Table = 'code'
Page_Content_Table = 'page_content'


Admin_Columns = ['id','email','password','payment']
Meeting_Columns = ['id', 'admin_id', 'start_at', 'name', 
                    'zoom_meeting_id', 'zoom_meeting_password', 
                    'ticket_count', 'price', 'page_url']
Code_Columns = ['id', 'event_id', 'is_used']
Page_Content_Columns = ['id', 'meeting_id', 'admin_id']