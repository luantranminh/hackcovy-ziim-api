from flask import Flask, redirect, url_for, request
from admin.controller import update_zoom_meeting, get_zoom_meeting

from user.controller import user_blueprint
app = Flask(__name__)

app.register_blueprint(user_blueprint)

@app.route('/send_zoom_meeting_id_pass',methods = ['POST'])
def send_zoom_meeting_id_pass():
    if request.method == 'POST':
        admin_email = request.form['admin_email']
        meeting_id = request.form['meeting_id']
        zoom_meeting_id = request.form['zoom_meeting_id']
        zoom_meeting_password = request.form['zoom_meeting_password']
    #   return redirect(url_for('success',meeting_id = meeting_id, password = password))
        # admin_email, meeting_id, zoom_meeting_id, zoom_meeting_password = 'first_admin@gmail.com', 2, 'meeting_id', 'new_pass2'
        return {'update':update_zoom_meeting(admin_email, meeting_id, zoom_meeting_id, zoom_meeting_password)}
    else:
        admin_email = request.args.get('admin_email')
        meeting_id = request.args.get('meeting_id')
        zoom_meeting_id = request.args.get('zoom_meeting_id')
        zoom_meeting_password = request.args.get('zoom_meeting_password')
    #   return redirect(url_for('success',meeting_id = meeting_id, password = password))
        # admin_email, meeting_id, zoom_meeting_id, zoom_meeting_password = 'first_admin@gmail.com', 2, 'meeting_id', 'new_pass2'
        return {'update':update_zoom_meeting(admin_email, meeting_id, zoom_meeting_id, zoom_meeting_password)}

@app.route('/get_zoom_meeting_id_pass',methods = ['GET'])
def get_zoom_meeting_id_pass():
    meeting_id = request.args.get('meeting_id')
    zoom_meeting_id, zoom_meeting_password = (get_zoom_meeting(meeting_id))
    return {'zoom_meeting_id':zoom_meeting_id,
            'zoom_meeting_password':zoom_meeting_password}

@app.route('/save_page',methods = ['POST'])
def save_page():
    if request.method == 'POST':
        admin_email = request.form['admin_email']
        name = request.form['name']
        ticket_count = request.form['ticket_count']
        price = request.form['price']
        page_url = request.form['page_url']
        return {'update':create_update_admin_page(admin_email,name,ticket_count,price,page_url)}

@app.route('/generate_code',methods = ['GET'])
def generate_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

if __name__ == '__main__':
    app.run("localhost", 1411, threaded=True, debug=True)