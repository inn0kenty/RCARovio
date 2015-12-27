from utils.http import HTTPRequests
import time
from datetime import datetime
import os
from utils.utils import Config
import subprocess
import threading


class Rovio(object):
    def __init__(self, address, commands):
        self.__address = address
        self.__commands = commands
        self.__remote_rovio = HTTPRequests(address)
        self.__remote_rovio.add_image_handler(self.__impage_handler)
        self.__config = Config()
        self.__remote_rovio.open()
        self.__remote_rovio.set_resolution(self.__config.get('resolution'))
        self.__remote_rovio.close()

    def do(self):
        with self.__remote_rovio as r:
            for command in self.__commands:
                if command.get_name() == 'capture_image':
                    done = r.cap_image()
                    continue

                if command.get_name() == 'wait':
                    time.sleep(command.get_time())
                    done =True
                    continue

                if command.get_time() < 0:
                    done = r.move(command)
                    time.sleep(0.5)
                    continue

                for t in xrange(command.get_time()*4):
                    done = r.move(command)
                    if not done:
                        break
                    time.sleep(0.15)

                if done:
                    print command.get_name() + '... done'

    def __impage_handler(self, data):
        handler = ImageHandler(data)
        handler.start()


class ImageHandler(threading.Thread):
    def __init__(self, image_data):
        threading.Thread.__init__(self)
        self.__image_data = image_data

    def run(self):
        image_path = os.getenv("HOME") + '/.rovio/'
        if not os.path.exists(image_path):
                os.makedirs(image_path)
        image_name = image_path + \
            datetime.now().strftime("%Y-%m-%d-%H-%M-%S.jpg")

        image = open(image_name, 'wb')
        image.write(self.__image_data)
        image.close()

        print 'capture_image ... done'

        config = Config()
        subprocess.call(config.get('open') + ' ' +
                        image_name + ' > /dev/null 2>&1', shell=True)
