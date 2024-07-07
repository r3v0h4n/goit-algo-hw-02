from queue import Queue
from request import Request

class RequestQueue():
    def __init__(self) -> None:
        self.queue = Queue()

    def generate_request(self, id: str, title: str) -> None:
        request = Request(id, title)
        self.queue.put(request)

    def process_request(self) -> None:
        if (self.queue.empty()):
            print("Queue is empty!")
            return
        
        request = self.queue.get()
        request.process()