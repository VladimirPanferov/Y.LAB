from places import AbstractCity


class SavePlace:
    def __init__(self, hero, place: AbstractCity, media) -> None:
        self.hero = hero
        self.place = place
        self.media = media

    def find(self) -> str:
        return self.place.get_antagonist()

    def save_the_place(self) -> None:
        self.find()
        self.hero.attack()
        self.media.create_news()