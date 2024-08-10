from fasthtml.common import *
from fh_frankenui.foundations import *
from enum import Enum, EnumMeta, EnumType
import string

__all__ = [ 'BaseEnum', 'CoreEnum', 'C']

def C(*args): return ' '.join(map(str,args))

class BaseEnum(Enum):
    def __add__(self, other):
        return self.__str__() + other.__str__()
    
    def __str__(self):
        return self.C()
    
    def C(self):
        base = self.__class__.__name__       
        if isinstance(self.__class__, EnumType):
            base = base.rstrip(string.ascii_uppercase).rstrip('_')
        return f"uk-{base.lower()}-{self.value}".strip('-')

class CoreEnum(BaseEnum):
    def __init__(self, name):
        if isinstance(name, str): pass
        else:
            for enm in name:
                self.__setattr__(enm.name, enm)