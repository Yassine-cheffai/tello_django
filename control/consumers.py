import json

from channels.generic.websocket import WebsocketConsumer
import time

from control.views import tello


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print("connection accepted")
        self.accept()
        self.send(text_data=json.dumps({"message": "connected"}))
        # while True:
        #     try:
        #         battery = tello.get_battery()
        #         self.send(text_data=json.dumps({"battery": battery}))
        #         time.sleep(2)
        #     except Exception as e:
        #         print(e)
        #         break

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        # pass
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print(message)
        battery = tello.get_battery()
        self.send(text_data=json.dumps({"battery": battery}))
