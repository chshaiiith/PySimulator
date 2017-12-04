import Queue
import stats


# XXX: Override the comparator of priority queue to support our functionality

Q = Queue.PriorityQueue()
time = 0
required_request_count = 0

def schedule(event):
        Q.put((event["time"], event))


def run(no_of_request = None):
    global time
    global required_request_count

    required_request_count = no_of_request

    if no_of_request:
        while not Q.empty():
            time, event = Q.get()
            event["callback"](event)

    reset()

    return

def reset():
    stats.print_stat()
    stats.global_reset()
    global time
    time = 0
    while not Q.empty():
        temp = Q.get()

    # Resetting request count
    global current_request_count
    current_request_count = 0

    # Little hack not a good way but it works
    # XXX: Reseting the completion time of servers here . Circular dependencies :-(
    # XXX: Ideally we should reset it for request_handler not request_handler_fifo. Very small thing do ASAP

    import request_handler_fifo
    request_handler_fifo.reset()


    return