import httplib
import urllib


class HTTPRequests (object):
    def __init__(self, ip):
        self.__ip = ip
        self.__image_handler = None

    def add_image_handler(self, image_handler):
        self.__image_handler = image_handler

    def move(self, speed, time):
        pass

    def cap_image(self):
        file_name = ""
        if self.__image_handler:
            self.__image_handler(file_name)

    def ping(self):
        connection = httplib.HTTPConnection(self.__ip, timeout=10)

        params = urllib.urlencode([('Cmd', 'nav'), ('action', 1)])
        try:
            connection.request('POST', '/rev.cgi', params)
            response = connection.getresponse()
        except:
            print 'Ping error\nConnection failed'
            connection.close()
            return False, None

        # parsing response
        response = response.read().strip('\n')
        connection.close()

        # response parameter
        ping = response.split('\n')[1].split('|')[0].split('=')
        # battery parameter
        battery = response.split('\n')[7].split('|')[1].split('=')

        if int(ping[1]) == 0:  # if response parameter 0 then all ok
            return True, battery[1]
        else:
            return False, None
