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
    data = json.load(open("creds.json", mode="r"))
    token = data["token"]
    myid = data["my_id"]
    test = Wrapper(token)
    x = test.send_tel("Hello", myid)
    print (x)

if __name__ == '__main__':
    main()
