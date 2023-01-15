import logging


logging.basicConfig( level=logging.DEBUG, format='%(asctime)s %(message)s')
#logging.basicConfig(filename='mylogfile.log', filemode='w', level=logging.DEBUG, format='%(asctime)s %(message)s')
#logging.Logger.setLevel(level=logging.DEBUG)
logging.info('info level is the lowest logging level, for normal program execution events')
logging.debug('debug same as info but with more detail')
logging.warning('warning')
logging.error('error')
logging.critical('critical')