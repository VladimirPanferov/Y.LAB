from time import time


def execution_time(func):
    def wrapper(*args, **kwargs):
        t1= time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"{args=}, {kwargs=} {result=} executed in {(t2-t1):.8f}s")
        return result
    return wrapper    


def memo(func):
    values = {}
    def wrapper(*args, **kwargs):
        key = args + tuple(kwargs.items())
        if key not in values:
            values[key] = func(*args, **kwargs)
        return values[key]
    return wrapper


@execution_time
@memo
def multiplier(number: int) -> int:
    return number * 2


def main():
    multiplier(99)
    multiplier(98)
    multiplier(99)


if __name__ == "__main__":
    main()