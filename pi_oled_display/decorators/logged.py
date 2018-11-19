from functools import wraps
from pi_oled_display.logger import logger


def logged(func):
    @wraps(func)
    def inner(*args, **kwargs):
        return_value = func(*args, **kwargs)
        logger.debug("Executing method {}, result {}".format(func.__name__, return_value))
        return return_value
    return inner
