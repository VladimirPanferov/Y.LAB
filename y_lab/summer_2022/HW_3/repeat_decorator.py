import time


def get_sleep_time(sleep_time, start_sleep_time, border_sleep_time, factor, num):
    if sleep_time < border_sleep_time:
        return start_sleep_time * (factor ** num)
    return border_sleep_time


def get_log_string(num, sleep_time, result):
    return f"Запуск номер {num}. Ожидание: {sleep_time} секунд. Результат декорируемой функций = {result}."


def repeat_decorator(*, call_count=1, start_sleep_time=1, factor=1, border_sleep_time=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Количество запусков {call_count}\nНачало работы")
            sleep_time = start_sleep_time
            for num in range(1, call_count+1):
                time.sleep(sleep_time)
                result = func(*args, **kwargs)
                print(get_log_string(num, sleep_time, result))
                sleep_time = get_sleep_time(
                    sleep_time=sleep_time,
                    start_sleep_time=start_sleep_time,
                    border_sleep_time=border_sleep_time,
                    factor=factor,
                    num=num
                )
            print("Конец работы")
            return result
        return wrapper
    return decorator


@repeat_decorator(call_count=6, start_sleep_time=1, factor=2, border_sleep_time=90)
def multiplier(number: int):
    return number * 2


def main():
    print(multiplier(10))


if __name__ == '__main__':
    main()
