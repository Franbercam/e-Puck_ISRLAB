"""
    Implementation of the third layer controller
    according to the hierchical agent architecture
"""

from typing import Any

class Controller:
    _state: Any

    def __init__(self):
        pass

    def plan(self, perceptions):
        """
        Planning algorithm for the robot to navigate
            1. read perceptions
            2. decide a new direction
            3. outpun the action
        :return:
        """
        ratio = perceptions[1] - perceptions[0]
        print("ratio:", ratio)
        if ratio == 0 :
            return 'right'
        else:
            return 'forward'

