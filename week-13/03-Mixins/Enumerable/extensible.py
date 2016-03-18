class Extensible:
    def __add__(self,other):
        iter_one = list(self.__iter__())
        iter_two = list(other.__iter__())
        return iter_one + iter_two