from Utility.Settings import *
class DeltaTime:
    def __init__(self, clock):
        self.__clock = clock
        self._delta_time = 0

    def update(self):
        self.delta_time = self.__clock.tick() / 1000
        return self.delta_time

    def get(self):
        return self._delta_time

    def set(self, value):
        self._delta_time = value

    def del_(self):
        del self._delta_time

    delta_time = property(get, set, del_)


