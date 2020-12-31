# -*- coding: utf-8 -*-

import requests
import json


class Wrapper():
    def __init__(self, token):
        self.base = "https://api.telegram.org/bot{}".format(token)

    def send_tel(self, text, chatid):
        url = self.base + "/sendMessage"
        params = {
                   "text": text,
                   "chat_id": chatid,
                   }
        r = requests.get(url, params=params)
        return json.loads(r.content)

def main():
    token = "Insert Token here"
    test = Wrapper(token)
    myid = "Insert ID here"
    x = test.send_tel("Hello", myid)
    print (x)

if __name__ == '__main__':
    main()
