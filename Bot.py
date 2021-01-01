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
        # TODO: Revisit and add additional params
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
        # TODO: Revisit and add additional params
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
        # TODO: Revisit and add additional params
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
        # TODO: Revisit and add additional params
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
        # TODO: Revisit and add additional params
        url = self.base + "/sendPhoto"
        params = {
                  "chat_id": chatId,
                  "caption": caption,
                  "disable_notification": disableNotifiation,
        }
        file = {"photo": open(filename, "rb")}
        r = requests.post(url, data=params, files=file)
        return json.loads(r.content)

    def send_audio(self, chatId, filename, caption=None, disableNotifiation=False):
        """
        Comment: send a audio message to a chat by chatId
        Input: Name of Instance, chatId, filename, optional: caption, disableNotifiation
        Output: Server Response as Json
        Special: You may Send .mp4 and .mp3 with up to 50MB
        """
        # TODO: Revisit and add additional params
        url = self.base + "/sendAudio"
        data = {
                "chat_id": chatId,
                "caption": caption,
                "disable_notification": disableNotifiation,
        }
        file = {"audio": open(filename, "rb")}
        r = requests.post(url, data=data, files=file)
        return json.loads(r.content)

    def send_document(self, chatId, filename, caption=None, disableNotifiation=False):
        """
        Comment: send a document to a chatId by it's filename
        Input: Name of Instance, chatId, filename, optional: caption, disableNotifiation
        Output: Server Response as Json
        Special: You may send files with up to 50MB
        """
        # TODO: Revisit and add additional params
        url = self.base + "/sendDocument"
        data = {
                "chat_id": chatId,
                "caption": caption,
                "disable_notification": disableNotifiation,
        }
        file = {"document": open(filename, "rb")}
        r = requests.post(url, data=data, files=file)
        return json.loads(r.content)

    def send_video(self, chatId, filename, caption=None, disableNotifiation=False):
        """
        Comment: send a video by it's filename to a chatId
        Input: Name of Instance, chatId, filename, optional: caption, disableNotifiation
        Output: Server Response as Json
        Special: You may send .mp4 with up to 50MB
        """
        # TODO: Revisit and add additional params
        url = self.base + "/sendVideo"
        data = {
                "chat_id": chatId,
                "caption": caption,
                "disable_notification": disableNotifiation,
        }
        file = {"video": open(filename, "rb")}
        r = requests.post(url, data=data, files=file)
        return json.loads(r.content)

    def send_animation(self, chatId, filename, caption=None, disableNotifiation=False):
        """
        Comment: send an animation by it's filename to a chatId
        Input: Name of Instance, chatId, filename, optional: caption, disableNotifiation
        Output: Server Response as Json
        Special: You may send .gif and h.264 without Sound with up to 50MB, only tested with .gif
        """
        # TODO: Revisit and add additional params
        url = self.base + "/sendAnimation"
        data = {
                "chat_id": chatId,
                "caption": caption,
                "disable_notification": disableNotifiation,
        }
        file = {"animation": open(filename, "rb")}
        r = requests.post(url, data=data, files=file)
        return json.loads(r.content)

    def send_voice(self, chatId, filename, caption=None, disableNotifiation=False):
        """
        Comment: send a voice message by it's filename to a chatId
        Input: Name of Instance, chatId, filename, optional: caption, disableNotifiation
        Output: Server Response as Json
        Special: You have to send a OPUS encoded .ogg file with max 50MB
        """
        url = self.base + "/sendVoice"
        data = {
                "chat_id": chatId,
                "caption": caption,
                "disable_notification": disableNotifiation,
        }
        file = {"voice": open(filename, "rb")}
        r = requests.post(url, data=data, files=file)
        return json.loads(r.content)

    # TODO: Add send_voice, send_video_note and send_media_group
    def send_location(self, chatId, long, lat, horizontalAccuracy=None, disableNotifiation=False, livePeriod=None, heading=None):
        """
        Comment: send a location by it's longitude and latitude to a chatId
        Input: Name of Instance, longitude, latitude, optional: accuracy and disableNotifiation
        Output: Server Response as Json Object
        Special: Nothing special
        """
        # TODO: Revisit and add additional params
        # TODO: Live Location not working, fix later.
        url = self.base + "/sendLocation"
        params = {
                  "chat_id": chatId,
                  "longitude": long,
                  "latitude": lat,
                  "horizontal_accuracy": horizontalAccuracy,
                  "disable_notification": disableNotifiation,
        }
        r = requests.get(url, params=params)
        return json.loads(r.content)
     # TODO: Add edit and stop Live location
    def send_venue(self, chatId, long, lat, title, adress):
        """
        Comment: Send a venue to a user
        Input: # TODO: finish docu
        Output:
        Special:
        """
        # TODO: Revisit and add additional params
        url = self.base + "/sendVenue"
        params = {
                  "chat_id": chatId,
                  "longitude": long,
                  "latitude": lat,
                  "title": title,
                  "adress": adress,
        }
        r = requests.get(url, params=params)
        return json.loads(r.content)
    # TODO: Add send_contact
    def send_poll(self, chatId, question, options, correctOptionId=None, type=None, explanation=None, disableNotifiation=False):
        """
        Comment: send a poll
        Input: Name of Instance, chatId, question, options (a List with options), optional: correctOptionId (correct answer if type=="quiz" as index from options), type of poll (either "regular" or "quiz")
        Output: Server Response as Json
        Special: If type=="regular", correctOptionId must be specified
        """
        # TODO: Complete further Params
        url = self.base + "/sendPoll"
        params = {
                  "chat_id": chatId,
                  "question": question,
                  "options": json.dumps(options),
                  "correct_option_id": correctOptionId,
                  "type": type,
                  "explanation": explanation,
                  "disable_notification": disableNotifiation,
        }
        r = requests.get(url, params=params)
        return json.loads(r.content)

    # def send_dice(self, chatId, disableNotifiation=False):



def main():
    data = json.load(open("creds.json", mode="r"))
    token = data["token"]
    myid = data["my_id"]
    test = Wrapper(token)
    x = test.send_voice(myid, "sample.ogg", "just a test", True)
    # for i in x["result"]:
    print (x)


if __name__ == '__main__':
    main()
