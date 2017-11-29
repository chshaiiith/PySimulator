from request_handler_fifo import RequesthandlerFiFo
from request_handler_priority import RequesthandlerPriority
import json

class Requesthandler:
    @classmethod
    def get_handler(self):
        with open("properties.json") as fp:
            config = json.load(fp)

        allowed = config["request"]["cancellation"]
        if not allowed:
            return RequesthandlerFiFo()

        else:
            return RequesthandlerPriority()

