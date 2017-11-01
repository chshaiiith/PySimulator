from distribution import Distribution
from arrival import Arrival
from request import Request
from request_handler import Requesthandler


import simulator

class RequestStream():
    def __init__(self):
        self.arrival = Arrival()
        self.request = Request()

        self.req_handler =  Requesthandler()

        self.add_arrival_event()



    def add_arrival_event(self):
        request = self.request.next_request()
        request["start_time"] = self.arrival.next_arrival()


        event = {
            "request" : request,
            "time": request["start_time"],
            "callback" : callback,
            "stream": self

        }

        simulator.schedule(event)
        return


def callback(event):
    event["stream"].req_handler.add_request(event["request"])
    event["stream"].add_arrival_event()

    return