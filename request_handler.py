import Queue
import json
import random
import simulator
from allocation_policy import AllocationPolicy

event_map = {}
class Requesthandler:
    def __init__(self):
        with open("properties.json") as fp:
            config = json.load(fp)

        # self.q = Queue.Queue()
        # # current completion time of a queue
        policy = config["server"]["allocationPolicy"]
        self.allocation_policy = AllocationPolicy.get_policy(policy)

        # TODO : Use this code if we want to use multiple queues
        self.write_server = config["server"]["writeServer"]
        self.read_server = config["server"]["readServer"]
        self.no_of_read_response_required = config["server"]["noOfReadResponse"]
        self.no_of_write_response_required = config["server"]["noOfWriteResponse"]

        self.server_queues = []
        self.completion_time = []

        for i in range(0, config["server"]["numberOfServers"]):
            self.server_queues.append(Queue.Queue())
            self.completion_time.append(0)



    def add_request(self, request):

        # Todo: Make it for both read and write . Currently all request read type
        servers = self.allocation_policy.get_server("read")

        for i in servers:
            self.server_queues[i].put(request)

            if self.completion_time[i] > simulator.time:
                self.completion_time[i] = self.completion_time[i] + request["request_size"]
            else:
                self.completion_time[i] = simulator.time + request["request_size"]

            event = {
                "time": self.completion_time[i],
                "request": request,
                "callback": callback
            }


            simulator.schedule(event)


def callback(event):
    global event_map

    with open("properties.json") as fp:
        config = json.load(fp)

    # I assumed Type1 is read request
    if event["request"]["type"] == "Type1":
        no_of_request_required = config["server"]["noOfReadResponse"]
        total_request = config["server"]["readServer"]
    else:
        no_of_request_required = config["server"]["noOfWriteResponse"]
        total_request = config["server"]["writeServer"]

    # Processing of request and deleting once we reached max
    if event["request"]["id"] in event_map:
        event_map[event["request"]["id"]] = event_map[event["request"]["id"]] + 1
    else:
        event_map[event["request"]["id"]] = 1

    if event_map[event["request"]["id"]] == no_of_request_required:
        total_time_for_request = event["time"] - event["request"]["start_time"]
        print total_time_for_request
        print event["request"]["id"]
    elif event_map[event["request"]["id"]] == total_request:
        del event_map[event["request"]["id"]]


    return
