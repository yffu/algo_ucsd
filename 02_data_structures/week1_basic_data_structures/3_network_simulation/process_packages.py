# python3

from collections import namedtuple
import os

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])
debug = True
directory = 'tests'

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        # output the answers for the packets in the same order as the packets are given in the input
        # need to have state of queue when the new request comes in, and when its response is finished
        # if debug: print('before: ' + str(self.finish_time) + '; request at: ' + str(request.arrived_at))
        while self.finish_time and self.finish_time[0] <= request.arrived_at:
            # print('finish_time: ' + str(self.finish_time[0]))
            self.finish_time.pop(0)
        # if debug: print('after: ' + str(self.finish_time))
        if len(self.finish_time) == self.size:
            return Response(True, -1)
        elif len(self.finish_time) == 0:
            self.finish_time.append(request.arrived_at + request.time_to_process)
            return Response(False, request.arrived_at)
        else:
            last_finish = self.finish_time[-1]
            # print ('last finish: ' + str(last_finish))
            self.finish_time.append(last_finish + request.time_to_process)
            return Response(False, last_finish)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses

# def main(text):
def main():
    # buffer_size, n_requests = map(int, text.readline().split())
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        # arrived_at, time_to_process = map(int, text.readline().split())
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    # f = os.path.join(directory, '19')
    # text = open(f, 'r')
    # a = open(f + '.a', 'r').read()
    # if debug:
    #     print('filename: ' + f)
    #     print('answer: ')
    #     print(a)
    #     main(text)
    main()
