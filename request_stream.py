from distribution import Distribution
from arrival import Arrival
from request import Request
from request_handler import Requesthandler
import json


import simulator

class RequestStream():
    def __init__(self, type = None):
        self.type = None
        if type:
            self.type = type
        else:
            # Just to verify if the
            with open("properties.json") as fp:
                config = json.load(fp)
            self.type = config["request"]["type"]

        self.arrival = Arrival()
        self.request = Request(type)

        self.req_handler =  Requesthandler.get_handler()

        self.add_arrival_event()

    def update_type(self, type):
        self.type = None
        if type and type != "default":
            self.type = type
        else:
            # Just to verify if the
            with open("properties.json") as fp:
                config = json.load(fp)
            self.type = config["request"]["type"]

        # Re-assigning the request based on the variable
        self.request = Request(type)
        self.add_arrival_event()


    def add_arrival_event(self):
        request = self.request.next_request()
        request["start_time"] = self.arrival.next_arrival()


        event = {
            "request" : request,
            "time": request["start_time"],
            "callback" : callback,
            "stream": self,
            "type": "arrival"

        }

        simulator.schedule(event)
        return


def callback(event):
    event["stream"].req_handler.add_request(event["request"])

    if simulator.required_request_count > 0:
        simulator.required_request_count -= 1
        event["stream"].add_arrival_event()

    return