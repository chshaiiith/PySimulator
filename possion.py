from numpy.random import exponential

import time
class Possion():
    def __init__(self, **kwargs):
        self.rate = kwargs["rate"]

    def next(self):
        data = exponential(1.0/self.rate)
        return data