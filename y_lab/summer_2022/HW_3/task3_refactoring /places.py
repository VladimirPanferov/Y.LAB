from abc import (
    ABC,
    abstractmethod,
)


class AbstractCity(ABC):
    @property
    def name(self):
        return self.name

    @abstractmethod
    def get_antagonist(self):
        pass


class Kostroma(AbstractCity):
    name = 'Kostroma'

    def get_antagonist(self):
        print('Orcs hid in the forest')


class Tokyo(AbstractCity):
    name = 'Tokyo'

    def get_antagonist(self):
        print('Godzilla stands near a skyscraper')
