from abc import ABC, abstractmethod
import json

class Saver(ABC):

    @abstractmethod
    def save(self, data: list):
        pass

class JSONSaver(Saver):

    def __init__(self, f_path):
        self.f_path = f_path

    def save(self, data: list):
        dumped_data = json.dumps(data)


        



