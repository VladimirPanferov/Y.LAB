from typing import (
    Iterable,
    NoReturn
)


class CyclicIterator:
    def __init__(self, stop_value: Iterable) -> None:
        self.current = -1
        self.stop_value = max(*stop_value)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop_value:
            self.current += 1
            return self.current
        self.current = -1
        self.__next__()
        return self.current


def main() -> NoReturn:
    cyclic_iterator = CyclicIterator(range(3))
    for i in cyclic_iterator:
        print(i)


if __name__ == '__main__':
    main()
