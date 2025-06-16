import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(
            f"function: {func.__name__}\n"
            f"positional parameters: {args if args else 'none'}\n"
            f"keyword parameters: {kwargs if kwargs else 'none'}\n"
            f"return: {result}\n"
        )
        return result
    return wrapper


@logger_decorator
def greeting():
    print("Hello World!")


@logger_decorator
def pos_args(*args):
    return True

@logger_decorator
def keyword_args(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    greeting()
    pos_args(17, 4, 64)
    keyword_args(a=2, b=7)
