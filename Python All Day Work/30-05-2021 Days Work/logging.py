
# Python - Logging


import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')


name = 'John'

logging.error('%s raised an error', name)

logging.basicConfig(filename='test.log', level=logging.DEBUG)


logging.debug('Debug message')
logging.info('Info message')
logging.error('Error message')
logging.critical('Critical message')


a = 10
b = 0

logging.info('Division Process Starting')
try:
    div = a/b
    print(div)
except ZeroDivisionError as e:
    logging.exception(e)
logging.info('Division Completed')
print('Hello')
logging.info('all done')

