import httplib
import urllib


class HTTPRequests (object):
    def __init__(self, ip):
        self.__ip = ip
        self.__image_handler = None

    def add_image_handler(self, image_handler):
        self.__image_handler = image_handler

    def move(self, command):
        params = urllib.urlencode([('Cmd', 'nav'), ('action', 18),
                                   ('drive', command.get_value()),
                                   ('speed', command.get_speed())])

        try:
            self.__connection.request('POST', '/rev.cgi', params)
            response = self.__connection.getresponse()
        except:
            print 'Connection failed'
            return False

        # parsing response
        response = response.read().strip('\n')

        # response parameter
        response = response.split('\n')[1].split('|')[0].split('=')
        if int(response) != 0:
            print 'Bad response from Rovio\nInternal error'
            return False

        return True

    def cap_image(self):
        file_name = ""
        if self.__image_handler:
            self.__image_handler(file_name)

    def ping(self):
        params = urllib.urlencode([('Cmd', 'nav'), ('action', 1)])
        try:
            self.__connection.request('POST', '/rev.cgi', params)
            response = self.__connection.getresponse()
        except:
            print 'Ping error\nConnection failed'
            return False, None

        # parsing response
        response = response.read().strip('\n')

        # response parameter
        ping = response.split('\n')[1].split('|')[0].split('=')
        # battery parameter
        battery = response.split('\n')[7].split('|')[1].split('=')

        if int(ping[1]) == 0:  # if response parameter 0 then all ok
            return True, battery[1]
        else:
            return False, None


    def open(self):
        self.__connection = httplib.HTTPConnection(self.__ip, timeout=10)

    def close(self):
        self.__connection.close()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, type, value, traceback):
        self.close()
