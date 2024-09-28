from logger import logging


logger1 = logging.getLogger('ArithmeticOp')

def add(a, b):
    result = a + b
    logger1.debug(f'Addition of {a} and {b} is taking place. Result is {result}')
    return a+b

def subtract(a, b):
    result = a - b
    logger1.debug(f'Subtraction of {a} and {b} is taking place. Result is {result}')
    return result

def multiply(a, b):
    result = a * b
    logger1.debug(f'Multiplication of {a} and {b} is taking place. Result is {result}')
    return result

def division(a, b):
    try:
        result = a / b
        logger1.debug(f'Addition of {a} and {b} is taking place. Result is {result}')
        return result
    except ZeroDivisionError:
        logger1.error(f'The Division of {a} and {b} results in error.')
        return result


add(10,5)
subtract(10,5)
multiply(10,5)
division(10,5)