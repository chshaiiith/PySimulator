import json

total_request = 0
total_time = 0
# Used for file numbering
total_files = 0
import os

class  Stats:
    def __init__(self):
        global f
        global file_name
        with open("properties.json") as fp:
            config = json.load(fp)

        file_name = config["stats"]["fileName"]
        self.no_of_request = config["stats"]["noOfRequest"]

        if os.path.exists(file_name + str(total_files)):
            os.remove(file_name + str(total_files))

        f = open(file_name + str(total_files), "a+")

    def collect_stats(self, event):
        global total_time
        global total_request

        total_time += event["time"] - event["request"]["start_time"]
        f.write(str(event["time"] - event["request"]["start_time"]) + " ")
        # print "stats: total_time " + str(event["time"] - event["request"]["start_time"])
        # print "stats: request time " + str(event["request"]["request_size"])

#        f.write(str(event["request"]["request_size"]) + " ")
        total_request += 1
        if total_request == self.no_of_request:
            print_stat()


def reset():
    global total_time
    global total_request
    total_time = 0
    total_request = 0


def global_reset():
    global total_files
    global f
    reset()
    f.close()
    total_files += 1
    if os.path.exists(file_name + str(total_files)):
        os.remove(file_name + str(total_files))

    f = open(file_name + str(total_files), "a+")

def print_stat():
    global total_request
    global total_request

    print total_time/total_request
    reset()