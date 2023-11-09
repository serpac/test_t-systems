from abc import abstractmethod

class MainServiceInterface:
    @abstractmethod
    def load_file(self, name_bucket: str, name_object:str, file: bytes):        pass

    @abstractmethod
    def get_file(self, name_bucket: str, name_object:str):        pass