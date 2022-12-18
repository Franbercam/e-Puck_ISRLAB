"""
    Implementation of the VirtualBody class of the Agent
"""

import json
import logging
import time
import redis
import Body

MY_PERCH_CH = "PERCEPTIONS"  # from the physical body to the virtual body and controller
MY_COMM_CH = "COMANDS"  # from virtual body to physical


class VirtualBody(Body.Body):

    def __init__(self, perception_channel, commands_channel):
        self._my_perc_ch = perception_channel
        self._my_comm_ch = commands_channel
        self._my_msg_broker = redis.Redis(decode_responses=True)
        self._my_perceptions = None
        try:
            print(self._my_msg_broker.info())
            self._pub_sub = self._my_msg_broker.pubsub()
            self._pub_sub.subscribe(self._my_perc_ch)
            msg = None
            while not msg:
                msg = self._pub_sub.get_message()
                time.sleep(0.1)
                print("Still waiting...")
            print("subscribed: ", msg, "to", self._my_perc_ch)
        except Exception as e:
            logging.exception(e)
            print(e)
            raise e

    def get_perceptions(self):
        while True:
            msg = self._pub_sub.get_message()
            if msg:
                self._my_perceptions = json.loads(msg['data'])
                return self._my_perceptions
            time.sleep(0.1)


    def send_command(self, command):
        try:
            self._my_msg_broker.publish(self._my_comm_ch, command)
        except Exception as e:
            print(e)
            raise e


if __name__ == "__main__":
    my_virtual_body = VirtualBody(MY_PERCH_CH, MY_COMM_CH)
    while True:
        percets = my_virtual_body.get_perceptions()
        print(percets)
        #command = my_virtual_body.plan(percets)
        #print(command)
        #my_virtual_body.send_command(command)
        time.sleep(0.1)
