import json
import uuid
import simulator
import numpy as np
import random


from distribution import Distribution

current_request_id = 0

class Request:
    def __init__(self, type):
        # To store ids of write request, will be used for read
        # All possible types
        self.types = ["read", "write"]

        with open("properties.json") as fp:
            config = json.load(fp)

        rate = config["job"]["rate"]
        self.distribution = Distribution.get_distribution(config["job"]["distribution"], rate = rate)

        #In case of mixed workload these variables represent the % of read and writes in workload
        self.type = type
        self.read_percentage = config["request"]["readPercentage"]
        self.write_percentage = config["request"]["writePercentage"]

        # Probability percentage
        self.probability_percentage = [self.read_percentage*1.0/100, self.write_percentage*1.0/100]
        # To store the sample request distribution based on type and probability
        self.request_distribution = []


    def next_request(self):
        request = None
        # In case of mixed workload
        if self.type == "mixed":
            if len(self.request_distribution) > 0:
                current_request_type = self.types[self.request_distribution[-1]]
                self.request_distribution = self.request_distribution[:-1]
            else:
                self.request_distribution = np.random.choice(2, 10000, p=self.probability_percentage)
                current_request_type = self.types[self.request_distribution[-1]]
                self.request_distribution = self.request_distribution[:-1]

            if current_request_type == "read":
                return self.get_read_request()

            else:
                return self.get_write_request()

        # In case of read workload
        elif self.type == "read":
            return self.get_read_request()

        # In case of write workload
        elif self.type == "write":
            return self.get_write_request()


        #Only return when request type is not read or write
        print "Not supported type is mentioned : Only {read, write} is supported"

        return request


    def get_read_request(self):
        global current_request_id
        id = random.randint(0 , current_request_id - 1)
        request = {"request_size": self.distribution.next(), "type": "read",
                   "id": id}

        return request


    def get_write_request(self):
        global current_request_id
        request = {"request_size": self.distribution.next(), "type": "write",
                   "id": current_request_id}
        current_request_id += 1

        return request