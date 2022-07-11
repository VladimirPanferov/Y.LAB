from abc import (
    ABC,
    abstractmethod,
)


class AbstractCity(ABC):
    """Some city"""
    @property
    def name(self):
        return self.name

    @abstractmethod
    def get_antagonist(self):
        """Get antagonist in  this place"""


class Kostroma(AbstractCity):
    """Kostroma city"""
    name = 'Kostroma'

    def get_antagonist(self):
        print('Orcs hid in the forest')


class Tokyo(AbstractCity):
    """Tokyo city"""
    name = 'Tokyo'

    def get_antagonist(self):
        print('Godzilla stands near a skyscraper')
