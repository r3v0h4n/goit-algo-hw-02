from queue import Queue
from request_queue import RequestQueue



def main():
    queue = RequestQueue()
    while True:
        command = input("Enter command (exit, generate, process): ")
        
        if command == 'exit':
            break
        elif command == 'generate':
            id = input("Enter request id: ")
            title = input("Enter request title: ")
            queue.generate_request(id, title)
        elif command == 'process':
            queue.process_request()

if __name__ == "__main__":
    main()