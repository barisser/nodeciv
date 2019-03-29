import economics
import math
import random
import resources
import settings


class Tile:
    def __init__(self, x, y, data):
        self.productivity = []
        for i in range(0, len(data['resources'])):
            self.productivity.append(random.random())
        self.x = x
        self.y = y

#    def consume(self, data):
