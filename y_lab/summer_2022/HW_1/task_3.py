from tkinter import N


def zeros(n: int) -> int:
    result = 0
    while n > 0:
        n //= 5
        result += n
    return result


def main() -> None:
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7


if __name__ == '__main__':
    main()
    
