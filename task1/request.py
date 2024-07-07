
class Request:
    def __init__(self, id: str, title: str):
        self.id = id
        self.title = title

    def process(self) -> None: 
        print(f"Request with id {self.id} and title {self.title} has been processed")