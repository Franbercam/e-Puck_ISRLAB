"""
    Main Hierchical Controller Agent
    Include:
        - VirtualBody communicating with the boy
          through the message broker
        - Controller comunicating internally with
          VirtualBody
"""

from VirtualBody import VirtualBody
from Controller import  Controller
import time

MY_PERCH_CH = "PERCEPTIONS"  # from the physical body to the virtual body and controller
MY_COMM_CH = "COMANDS"  # from virtual body to physical

if __name__ == "__main__":
    my_virtual_body = VirtualBody(MY_PERCH_CH, MY_COMM_CH)
    my_controller = Controller()
    while True:
        percets = my_virtual_body.get_perceptions()
        print(percets)
        command = my_controller.plan(percets)
        print(command)
        my_virtual_body.send_command(command)
        time.sleep(0.1)


