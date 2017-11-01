import json
import uuid
import simulator



from distribution import Distribution

class Request:
    def __init__(self):
        with open("properties.json") as fp:
            config = json.load(fp)

        self.distribution = Distribution.get_distribution(config["job"]["distribution"], rate = 3)

    def next_request(self):
        request = {"request_size" : self.distribution.next(), "type" : "Type1", "id": uuid.uuid4().hex[:6].upper()}
        return request