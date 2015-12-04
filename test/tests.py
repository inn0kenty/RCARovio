import httplib
import urllib

class Test(object):
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__available_commands = ('address')
    def syntax(self):
        print 'test'

    def battery(self):
        print '122'

    def ping(self):
        command_file = open(self.__file_path, 'r')
        command = command_file.readline().strip('\n')
        command_file.close()
        command = command.split(' ')

        if not (command[0] in self.__available_commands):
            print 'Ping error\nFile syntax error\naddress keyword not found'
            exit(-1)

        if not self.__is_ip_correct(command[1]):
            print 'Ping error\nFile syntax error\nip is incorrect'
            exit(-1)

        if not self.__request(command[1]):
            exit(-1)

        print 'Ping test OK'

    def __is_ip_correct(self, ip):
        ip = ip.split('.')

        if len(ip) != 4:
            return False

        for i in ip:
            if int(i) < 0 or int(i) > 255:
                return False

        return True

    def __request(self, ip):
        connection = httplib.HTTPConnection(ip, timeout=10)

        params = urllib.urlencode({'Cmd': 'nav', 'action': 1})
        try:
            connection.request('POST','/cgi-bin/rev.cgi', params)
        except :
            print 'Ping error\nConnection failed'
            connection.close()
            return False

        response = connection.getresponse()

        response = response.read().strip('\n')
        connection.close()

        response = response.split('\n')[1].split('|')[0].split('=')

        if int(response[1]) == 0:
            return True
        else:
            return False
