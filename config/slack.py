import requests
from config.mytoken import *

class Slack():
    def send_msg(self, msg=""):
        response = requests.post(
            'https://slack.com/api/chat.postMessage',
            headers={
                'Authorization': 'Bearer ' + mytoken()
            },
            data={
                'channel':'#realmessage',
                'text':msg
            }
        )
        print(response)