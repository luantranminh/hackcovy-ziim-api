from flask import Blueprint
import os
import base64
import random
import email_sender

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/payment')
def index():
    return "This is an example app"



def send_meeting_info_email(receiver_email):
    code = __generate_code()
    print(code)


def __generate_code(num_chars=6):
    code_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for i in range(0, num_chars):
        slice_start = random.randint(0, len(code_chars) - 1)
        code += code_chars[slice_start: slice_start + 1]
    return code

def __save_code():
    