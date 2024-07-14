from Utility.Settings import *
class PhysicsObject(ABC):
    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def update(self, delta_time):
        pass

