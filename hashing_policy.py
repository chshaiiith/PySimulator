import hashlib
import json

class HashingPolicy:
    def __init__(self):
        with open("properties.json") as fp:
            config = json.load(fp)

        self.number_of_servers = config["server"]["numberOfServers"]
        self.read_server = config["readServer"]
        self.write_server = config["writeServer"]


    def get_server(self, request):
        #XXX: Todo: Hashing based on some policy
        return []