from request_stream import RequestStream
import simulator

import request_handler_fifo



req_stream = RequestStream("write")
simulator.run(100000)

#print simulator.time
#print simulator.required_request_count

print "#######################\n"
print "Done with insertions. Now will perform required operations"
print "#######################\n"

req_stream.update_type("mixed")
simulator.run(100000)
