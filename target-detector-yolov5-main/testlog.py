import logging as log


log.basicConfig(filename='test.log',level=log.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
log.debug('Test logfile')