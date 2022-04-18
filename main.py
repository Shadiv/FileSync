import time
import dirsync
import Filesync


if __name__ == '__main__':
    file_sync = Filesync.Filesync()

    while True:
        dirsync.sync(file_sync.source, file_sync.replica, 'sync', logger=file_sync.logger)
        time.sleep(file_sync.sleep)


