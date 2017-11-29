import Queue
import json
import random
import simulator
from allocation_policy import AllocationPolicy
from stats import Stats
from arrival import Arrival
from distribution import Distribution

event_map = {}
class RequesthandlerPriority:
    def __init__(self):
        with open("properties.json") as fp:
            config = json.load(fp)

        # self.q = Queue.Queue()
        # # current completion time of a queue
        policy = config["server"]["allocationPolicy"]
        self.allocation_policy = AllocationPolicy.get_policy(policy)
        self.stat = Stats()


        # TODO : Use this code if we want to use multiple queues
        self.write_server = config["server"]["writeServer"]
        self.read_server = config["server"]["readServer"]
        self.no_of_read_response_required = config["server"]["noOfReadResponse"]
        self.no_of_write_response_required = config["server"]["noOfWriteResponse"]

        self.server_queues = []
        self.completion_time = []

        for i in range(0, config["server"]["numberOfServers"]):
            self.server_queues.append(Queue.PriorityQueue())
            self.completion_time.append(0)

        self.dist = Distribution.get_distribution(config["request"]["distribution"] , rate=1)

    def add_request(self, request):
        servers = self.allocation_policy.get_server(request["type"])

        for i in servers:
            self.server_queues[i].put(request)
            request["request_size"] = self.dist.next()
            print "priority size: " + request["id"] + " " + str(request["request_size"])
            if self.completion_time[i] > simulator.time:
                self.completion_time[i] = self.completion_time[i] + request["request_size"]
            else:
                self.completion_time[i] = simulator.time + request["request_size"]

            event = {
                "time": self.completion_time[i],
                "request": request,
                "callback": callback,
                "handler": self,
                "index": i
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

    # Processing of request and deleting once we reached max
    if event["request"]["id"] in event_map:
        event_map[event["request"]["id"]] = event_map[event["request"]["id"]] + 1
    else:
        event_map[event["request"]["id"]] = 1

    if event_map[event["request"]["id"]] == no_of_request_required:
        #print "reached here"
        event["handler"].stat.collect_stats(event)
        new_event = {
            "time": simulator.time,
            "callback": removal,
            "request": event["request"],
            "handler": event["handler"],
            "index": event["index"]
        }

        simulator.schedule(new_event)
    elif event_map[event["request"]["id"]] == total_request:
        del event_map[event["request"]["id"]]

    return


def removal(event):
    q = Queue.PriorityQueue()
    while not simulator.Q.empty():
        elem = simulator.Q.get()
        if elem[1]["request"]["id"] != event["request"]["id"]:
            q.put(elem)
    simulator.Q = q


