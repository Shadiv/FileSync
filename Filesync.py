import os
import sys
import logging

class Filesync:
    def __init__(self):
        self.source = input("Source path: ")
        self.replica = input("Replica path: ")
        self.sleep = input('Synchronization period (seconds, optional): ')

        #logger
        self.logger = logging.getLogger('Filesync')
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(message)s')
        hdl_stream = logging.StreamHandler(sys.stdout)
        hdl_stream.setFormatter(formatter)
        self.logger.addHandler(hdl_stream)
        hdl_file = logging.FileHandler('sync_log.log')
        hdl_file.setFormatter(formatter)
        self.logger.addHandler(hdl_file)

        # If period is not defined or incorrect, program will use standard period for synchronization - 10 sec.
        if self.sleep is None:
            self.sleep = 10
        else:
            try:
                self.sleep = int(self.sleep)
            except ValueError:
                print('Wrong period is set - using standard length')
                self.sleep = 10
        # Checking only source and logs directory. If replica directory is missing or incorrect, it will be created.
        # If logger directory is missing, logs will be stored in the source directory.
        while os.path.isdir(self.source) is False:
            self.source = input('Please, provide correct source path: ')
        while os.path.isdir(self.replica) is False:
            self.replica = input('Please, provide correct replica path: ')






