import main as main_two
import time
import logging

start_time = time.monotonic()
# Функция из п.1


def log(func):
    def wrap_log(*args, **kwargs):
        name = func.__name__
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler("%s.log" % name)
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        logger.info("Вызов функции: %s" % name)
        result = func(*args, **kwargs)
        logger.info("Результат: %s" % result)
        return func
    return wrap_log


@log
def double_function(a):
    return a


if __name__ == "__main__":
    value = double_function(main_two)
