from enumerable import Enumerable
from extensible import Extensible

class Collection(Enumerable, Extensible):
    def __init__(self, *args):
        self._container = args

    def __iter__(self):
        return iter(self._container)

    def __eq__(self, other):
        return list(self._container) == list(other.__iter__())