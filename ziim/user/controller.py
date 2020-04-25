from flask import Blueprint, jsonify, request
import os
import base64
import random
from . import email_sender
from database import db_helper

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/<event_id>/payment', methods=["POST"])
def pay(event_id):
    rcode = __save_code(event_id)
    data = request.get_json()
    if(not data):
        return jsonify({'error': 'missing body'}), 400

    receiver_email = data.get('email', '')

    res = __send_meeting_info_email(receiver_email, rcode)
    
    return jsonify({'message': res}), 200

@user_blueprint.route('/code_verification', methods=["GET"])
def check_code():
    data = request.get_json()
    if(not data):
        return jsonify({'error': 'missing body'}), 400

    code = data.get('code', '')
    event_id = data.get('event_id', '')

    check_exists_statement = """
            SELECT COUNT(1)
            FROM event_code
            WHERE code = '{0}' AND event_id = {1}
        """.format(code, event_id)
    is_exists = db_helper.is_exists(check_exists_statement)

    
    return jsonify({'message': is_exists}), 200



def __send_meeting_info_email(receiver_email, code):
    return email_sender.send_payment_success_email(receiver_email, code)


def __generate_code(num_chars=6):
    code_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for i in range(0, num_chars):
        slice_start = random.randint(0, len(code_chars) - 1)
        code += code_chars[slice_start: slice_start + 1]
    return code

def __save_code(event_id):

    is_exists = True
    code = ''
    while is_exists:
        code = __generate_code()
        check_exists_statement = """
                SELECT COUNT(1)
                FROM event_code
                WHERE code = '{0}'
            """.format(code)

        is_exists = db_helper.is_exists(check_exists_statement)
    
    inserted = False
    while not inserted:
        insert_statement = """ 
                INSERT INTO event_code(event_id, is_used, code) values ({0}, {1}, '{2}')
            """.format(event_id, 0, code)

        inserted = db_helper.insert(insert_statement)

    return code
