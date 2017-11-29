import Queue
import json
import simulator
from allocation_policy import AllocationPolicy
from stats import Stats
import sys
from distribution import Distribution


event_map = {}
request_to_server_map = {}
completion_time = []

class RequesthandlerFiFo:
    def __init__(self):
        global completion_time
        with open("properties.json") as fp:
            config = json.load(fp)

        policy = config["server"]["allocationPolicy"]
        self.allocation_policy = AllocationPolicy.get_policy(policy)
        self.stat = Stats()

        # Todo : Use this code if we want to use multiple queues
        self.write_server = config["server"]["writeServer"]
        self.read_server = config["server"]["readServer"]
        self.no_of_read_response_required = config["server"]["noOfReadResponse"]
        self.no_of_write_response_required = config["server"]["noOfWriteResponse"]

        self.server_queues = []

        for i in range(0, config["server"]["numberOfServers"]):
            self.server_queues.append(Queue.Queue())
            completion_time.append(0)
        rate = config["job"]["rate"]
        self.dist = Distribution.get_distribution(config["job"]["distribution"] , rate=rate)



    def add_request(self, request):
        global completion_time
        # Todo: Make it for both read and write. Currently all request read type
        if request["id"] in request_to_server_map:
            servers = self.allocation_policy.get_server(request["type"],
                                                        request_to_server_map[request["id"]])
       #     print servers
        else:
            servers = self.allocation_policy.get_server(request["type"])
            request_to_server_map[request["id"]] = servers

        for i in servers:
            request["request_size"] = self.dist.next()
        #    print "fifo size: " + str(request["id"]) + " " + str(request["request_size"])

            self.server_queues[i].put(request)

            if completion_time[i] > simulator.time:
                completion_time[i] = completion_time[i] + request["request_size"]
            else:
                completion_time[i] = simulator.time + request["request_size"]


            event = {
                "time": completion_time[i],
                "request": request,
                "callback": callback,
                "handler": self,
                "index": i,
                "type" : "completion"
            }

            simulator.schedule(event)


def callback(event):
    global event_map

    with open("properties.json") as fp:
        config = json.load(fp)

    # I assumed Type1 is read request
    if event["request"]["type"] == "read":
        no_of_request_required = config["server"]["noOfReadResponse"]
        total_request = config["server"]["readServer"]
    else:
        no_of_request_required = config["server"]["noOfWriteResponse"]
        total_request = config["server"]["writeServer"]

    # Processing of request
    current_queue = event["handler"].server_queues[event["index"]]
    current_request = current_queue.get()

    # Since it is FIFO this should to be true
    assert(current_request["id"] == event["request"]["id"])

    if event["request"]["id"] in event_map:
        event_map[event["request"]["id"]] = event_map[event["request"]["id"]] + 1
    else:
        event_map[event["request"]["id"]] = 1

    if event_map[event["request"]["id"]] == no_of_request_required:
        event["handler"].stat.collect_stats(event)

    if event_map[event["request"]["id"]] == total_request:
        del event_map[event["request"]["id"]]

    return

def reset():
    global completion_time
    for i in range(len(completion_time)):
        completion_time[i] = 0