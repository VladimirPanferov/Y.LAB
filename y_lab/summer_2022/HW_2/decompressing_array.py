from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, NoReturn, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        delta = timedelta(days=1)
        date1_start = self.dates[0][0]
        date1_end = self.dates[0][1]
        while date1_start <= date1_end:
            yield date1_start
            date1_start += delta
        date2_start = self.dates[1][0]
        date2_end = self.dates[1][1]
        while date2_start <= date2_end:
            yield date2_start
            date2_start += delta


def main() -> NoReturn:
    m = Movie('sw', [
    (datetime(2020, 1, 1), datetime(2020, 1, 7)),
    (datetime(2020, 1, 15), datetime(2020, 2, 7))
    ])

    for d in m.schedule():
        print(d)


if __name__ == '__main__':
    main()
    
