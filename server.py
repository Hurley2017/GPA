from flask import Flask, request
from bardapi import Bard
import os
from dotenv import load_dotenv

load_dotenv()


api = Flask(__name__)

@api.route('/', methods=['GET'])
def heartbeat():
    return "Yep! Alive..."


# @api.route('/getBard_Response', methods=['POST'])
# def returnB():
#     var = {'Content' : "bhag bsdk"}
#     API_key = os.environ.get('API_KEY')
#     ai = Bard(token=API_key)
#     Package = request.json
#     if Package['Key'] == os.environ.get('USR_KEY'):
#         test = ai.get_answer(Package['Query'])
#         var ["Content"]=test['content']  
#     return var

