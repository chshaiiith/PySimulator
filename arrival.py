from distribution import Distribution

import simulator
import json


class Arrival:
    def __init__(self):
        with open("properties.json") as fp:
            config = json.load(fp)
        rate = config["arrival"]["rate"]
        self.distribution = Distribution.get_distribution(config["arrival"]["distribution"] , rate=rate)

    def next_arrival(self):
        return self.distribution.next() + simulator.time
