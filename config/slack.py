import requests
from config.myInfo import *

class Slack():
    def __init__(self):
        self.myInfo = MyInfo()

    def send_msg(self, msg=""):
        response = requests.post(
            'https://slack.com/api/chat.postMessage',
            headers={
                'Authorization': 'Bearer ' + self.myInfo.token
            },
            data={
                'channel':'#realmessage',
                'text':msg
            }
        )
        print(response)