import random
import json
from operator import itemgetter

# Ideally it should be request handler .
# XXX: Move all global variables to request_handler than RequestFiFo Handler
import request_handler_fifo

class SJF:
    def __init__(self):
        with open("properties.json") as fp:
            config = json.load(fp)

        self.number_of_servers = config["server"]["numberOfServers"]
        self.read_server = config["server"]["readServer"]
        self.write_server = config["server"]["writeServer"]
        self.serverlist = [x for x in range(0, self.number_of_servers)]

    def get_server(self, type_of_request, possible_servers=None):
        if type_of_request == "read":
            count = self.read_server
            sorted_server = self.sort_server_on_completion_time(possible_servers)
            return sorted_server[:count]
        else:
            count = self.write_server
            sorted_server = self.sort_server_on_completion_time(self.serverlist)
      #      print request_handler_fifo.completion_time
       #     print sorted_server
            return sorted_server[:count]

    def sort_server_on_completion_time(self, servers):
        dict = []
        for server in servers:
            dict.append([request_handler_fifo.completion_time[server], server])

        data_list = sorted(dict, key=itemgetter(0))
        out = []
        for data in data_list:
            out.append(data[1])

        return out