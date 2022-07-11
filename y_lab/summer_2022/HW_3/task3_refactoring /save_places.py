from heroes import SuperHero

from places import AbstractCity

from news import Media


class SavePlace:
    """Interactions between hero and place"""

    def __init__(self, hero: SuperHero, place: AbstractCity, media: Media) -> None:
        self.hero = hero
        self.place = place
        self.media = media

    def find(self) -> str:
        """Find antagonist in the place"""
        return self.place.get_antagonist()

    def save_the_place(self) -> None:
        """Hero save the place"""
        self.find()
        self.hero.attack()
        self.media.create_news(f"Hero {self.hero.name} save {self.place.name}.")
