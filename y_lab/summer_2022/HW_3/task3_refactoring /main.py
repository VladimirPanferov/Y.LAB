from places import (
    Kostroma,
    Tokyo,
)

from save_places import SavePlace
from heroes import Superman, ChuckNorris
from news import Newspaper


if __name__ == '__main__':
    place = SavePlace(Superman(), Kostroma(), Newspaper("The New York Times"))
    place.save_the_place()
    print('-' * 20)
    place = SavePlace(ChuckNorris(), Tokyo(), Newspaper("The Daily Mirror"))
    place.save_the_place()
