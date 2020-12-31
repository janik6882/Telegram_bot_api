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

    def get_update(self, offset=None, limit=None):
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

    def forward_message(self, chatId, fromChatId, messageId, disableNotifiation=False):
        """
        Comment: forwards a message by its fromChatId and its messageId to a
               chatId
        Input: Name of Instance, chat to forward to, from chat, messageId, optional: disableNotifiation
        Output: Server Response as Json
        Special: Notification Sound can be disabled with disableNotifiation set to True
        """
        url = self.base + "/forwardMessage"
        params = {
                  "chat_id": chatId,
                  "from_chat_id": fromChatId,
                  "message_id": messageId,
                  "disable_notification": disableNotifiation,
        }
        r = requests.get(url, params=params)
        return json.loads(r.content)

    def copy_message(self, chatId, fromChatId, messageId, disableNotifiation=False):
        """
        Comment: copy a message and send it to another chat
        Input: Name of Instance, chatId, fromChatId, messageId, optional: disableNotifiation
        Output: Server Response as Json
        Special: Notification Sound can be disabled with disableNotifiation set to True
        """
        url = self.base + "/copyMessage"
        params = {
                  "chat_id": chatId,
                  "from_chat_id": fromChatId,
                  "message_id": messageId,
                  "disable_notification": disableNotifiation,
                }
        r = requests.get(url, params=params)
        return json.loads(r.content)

    def send_photo(self, chatId, filename, caption=None, disableNotifiation=False):
        """
        Comment: send a photo to a user specified by their chatId
        Input: Name of Instance, chatId, filename of the photo, optional: caption
        Output: Server Response as Json
        Special: max filesize: 10MB, max width and height: 10000
        """
        url = self.base + "/sendPhoto"
        params = {
                  "chat_id": chatId,
                  "caption": caption,
                  "disable_notification": disableNotifiation,
        }
        file = {"photo": open(filename, "rb")}
        r = requests.post(url, data=params, files=file)
        return json.loads(r.content)


def main():
    data = json.load(open("creds.json", mode="r"))
    token = data["token"]
    myid = data["my_id"]
    test = Wrapper(token)
    x = test.send_photo(myid, "test.jpg", "Dies ist ein Test", "True")
    # for i in x["result"]:
    print (x)


if __name__ == '__main__':
    main()
