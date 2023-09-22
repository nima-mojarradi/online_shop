import os
import pyotp
from datetime import datetime,timedelta
from kavenegar import KavenegarAPI
from rest_framework.exceptions import APIException


def send_otp_code(phone_number):    
    api = KavenegarAPI('{Your APIKey}')
    params = {
        'sender': '10004346',
        'receptor': '{Your Phone Number}',
        'message': 'Kaveh specialized Web service '
    }   
    response = api.sms_send(params)
    print(str(response))
