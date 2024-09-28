from logger import logging

def add(a, b):
    logging.debug('Addition is taking place')
    return a+b

logging.debug('Addtion function is being called')
add(10,5)