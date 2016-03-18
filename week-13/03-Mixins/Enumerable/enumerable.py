class Enumerable:
    def take(self, n): #take first n elements
        data = list(self.__iter__())
        return data[:n]

    def drop(self, n): # remove first n elements /start list from n->/
        data = list(self.__iter__())
        return data[n:]

    def take_while(self, predicate):
        data = self.__iter__()
        return [x for x in data if predicate(x)]

    def drop_while(self, predicate):
        data = self.__iter__()
        return [x for x in data if not predicate(x)]

    def map(self, callable):
        data = self.__iter__()
        return [callable(x) for x in data]

    def filter(self, predicate):
        data = self.__iter__()
        return [x for x in data if predicate(x)]

    def reduce(self, start_value, operator):
        data = self.__iter__()
        adding = start_value
        return sum([(x + adding) for x in data])

    # Returns True, if value is in self
    def search(self, value):
        data = list(self.__iter__())
        return value in data
