import sys
from Adafruit_IO import MQTTClient
from uart import *


class Adafruit_MQTT:
    AIO_FEED_IDs = ["nutnhan1", "nutnhan2"]
    AIO_USERNAME = ""
    AIO_KEY = ""

    # recvCallBack = None

    # def setRecvCallBack(self, func):
    #     self.recvCallBack = func

    def connected(self, client):
        print("Connected ...")
        for feed in self.AIO_FEED_IDs:
            client.subscribe(feed)

    def subscribe(self, client, userdata, mid, granted_qos):
        print("Subscribeb...")

    def publish(self, feed_id, value):
        self.client.publish(feed_id, value)

    def disconnected(self, client):
        print("Disconnected...")
        sys.exit(1)

    def message(self, client, feed_id, payload):
        # print("Received: " + payload)
        print("Received: " + payload + " , feed id: " + feed_id)
        if feed_id == "nutnhan1":
            if payload == "0":
                writeData("Nut nhan 1 off\n")
            else:
                writeData("Nut nhan 1 on\n")
        if feed_id == "nutnhan2":
            if payload == "0":
                writeData("Nut nhan 2 off\n")
            else:
                writeData("Nut nhan 2 on\n")

    # recvCallBack(payload)

    def __init__(self):
        self.client = MQTTClient(self.AIO_USERNAME, self.AIO_KEY)
        self.client.on_connect = self.connected
        self.client.on_disconnect = self.disconnected
        self.client.on_message = self.message
        self.client.on_subscribe = self.subscribe
        self.client.connect()
        self.client.loop_background()
