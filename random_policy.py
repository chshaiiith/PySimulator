import random
import json

class RandomPolicy:
    def __init__(self):
        with open("properties.json") as fp:
            config = json.load(fp)

        self.number_of_servers = config["server"]["numberOfServers"]
        self.read_server = config["server"]["readServer"]
        self.write_server = config["server"]["writeServer"]
        self.serverlist = [x for x in range(0, self.number_of_servers)]

    def get_server(self, type_of_request):
        if type_of_request == "read":
            count = self.read_server
        else:
            count = self.write_server

        return random.sample(self.serverlist, count)