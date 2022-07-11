from abc import (
    ABC,
    abstractmethod,
)


from weapons import (
    Laser,
    Gun,
    HandCombat,
)

class SuperHero(ABC):
    @property
    def name(self):
        pass

    @property
    def can_use_ultimate_attack(self):
        pass

    @abstractmethod
    def attack(self):
        pass


class Superman(SuperHero, Laser, HandCombat, Gun):
    name = "Clark Kent"
    can_use_ultimate_attack = True

    def attack(self):
        if self.can_use_ultimate_attack:
            self.incinerate_with_lasers()
        self.roundhouse_kick()


class ChuckNorris(SuperHero, Gun, HandCombat):
    name = "Chuck Norris"
    can_use_ultimate_attack = False

    def attack(self):
        self.fire_a_gun()
        self.roundhouse_kick()
