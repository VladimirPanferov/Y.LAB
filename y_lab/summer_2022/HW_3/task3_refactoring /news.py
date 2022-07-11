from abc import (
    ABC,
    abstractmethod,
)


class Media(ABC):
    """Some media"""

    @abstractmethod
    def create_news(self, news: str):
        """Print news"""


class Newspaper(Media):
    """Printing news in newspaper"""

    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def create_news(self, news: str):
        print(f"Print in {self.name}: {news}")
