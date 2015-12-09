from utils import http
import time
from datetimme import datetime
import os


class Rovio(object):
    def __init__(self, address, commands):
        self.__address = address
        self.__commands = commands
        self.__remote_rovio = http.HTTPRequests(address)
        self.__remote_rovio.add_image_handler(self.__impage_handler)

    def do(self):
        with self.__remote_rovio as r:
            for command in self.__commands:
                if command.get_name() == 'capture_image':
                    r.cap_image()
                    continue

                for t in xrange(command.get_time()):
                    if not r.move(command):
                        break
                    time.sleep(1000)

    def __impage_handler(self, data):
        image_path = os.getenv("HOME") + '/.rovio/'
        if not os.path.exists(image_path):
                os.makedirs(image_path)
        image_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S.jpg")

        image = open(image_path + image_name, 'wb')
        image.write(data)
        image.close()

        # TODO: add some command to show image
