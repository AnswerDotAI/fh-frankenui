from enum import Enum

class ObjectEnum(Enum):
    def __add__(self, other):
        return f"{self.__str__()} {other.__str__()}"

    def __str__(self):
        nm = self.__class__.__name__.lower()
        return f"uk-{nm} uk-{nm}-{self.value}"

class StyleEnum(Enum):
    def __add__(self, other):
        return FrankenStr(f"{self.__str__()} {other.__str__()}")
    
    def __str__(self):
        return f"uk-{self.__class__.__name__.lower()}-{self.value}"
    
class FrankenStr(str):
    def __add__(self, other):
        return FrankenStr(f"{self.__str__()} {other.__str__()}")
