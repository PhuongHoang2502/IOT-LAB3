from adafruit_mqtt import Adafruit_MQTT
import time
import random
from simple_ai import *
from uart import *

device1 = Adafruit_MQTT()

counter = 10
counter_ai = 5
ai_result = ""
previous_result = ""
while True:
    # counter = counter - 1
    # if counter <= 0:
    #     counter = 10
    #     # todo
    #     print("Random data is publishing...")
    #     temp = random.randint(25, 40)
    #     device1.publish("cambien1", temp)
    #     light = random.randint(100, 500)
    #     device1.publish("cambien2", light)
    #     humi = random.randint(40, 85)
    #     device1.publish("cambien3", humi)
    counter_ai = counter_ai - 1
    if counter_ai <= 0:
        counter_ai = 5
        previous_result = ai_result
        ai_result = image_detector()
        print("AI Output: ", ai_result)
        if previous_result != ai_result:
            device1.publish("ai", ai_result)
    readSerial(device1)
    time.sleep(1)
