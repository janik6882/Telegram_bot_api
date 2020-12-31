# -*- coding: utf-8 -*-

import requests
import json


class Wrapper():
    def __init__(self, token):
        self.base = "https://api.telegram.org/bot{}".format(token)
        working = self.get_me()["ok"]
        if not working:
            raise ValueError("token invalid, please check token")

    def get_me(self):
        """
        Comment: Function for testing your auth token
        Input: Name of Instance
        Output: True if token is valid, false if not
        Special: Nothing Special
        """
        url = self.base + "/getMe"
        r = requests.get(url)
        res = json.loads(r.content)
        return res

    def get_tells(self, offset=None, limit=None):
        """
        Comment: gets all recent messages sent to the bot by a certain offset
        Input: Name of instance, offset
        Output: Server Response with all received messages
        Special: offset is the first update_id which should be returned
        """
        url = self.base + "/getUpdates"
        params = {
                  "offset": offset,
                  "limit": limit,
        }
        r = requests.get(url, params=params)
        return json.loads(r.content)

    def send_message(self, text, chatId):
        """
        Comment: Sends a message to a specified Chat by the Chat_id
        Input: Name of Instance, text to send and the chat_id
        Output: Server Response
        Special: The user must first send a message to the bot before the bot
                can send messages to the user.
        """
        # TODO: Add optional Params from Doku
        url = self.base + "/sendMessage"
        params = {
                   "text": text,
                   "chat_id": chatId,
                   }
        r = requests.get(url, params=params)
        return json.loads(r.content)

    def forward_message(self, chatId, fromChatId, messageId):
        """
        Comment: forwards a message by its fromChatId and its messageId to a
               chatId
        Input: Name of Instance, chat to forward to, from chat, messageId
        Output: Server Response as Json
        Special:
        """



def main():
    data = json.load(open("creds.json", mode="r"))
    token = data["token"]
    myid = data["my_id"]
    test = Wrapper(token)
    x = test.get_me()
    # for i in x["result"]:
    print (x)


if __name__ == '__main__':
    main()
