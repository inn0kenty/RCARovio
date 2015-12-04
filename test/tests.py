import httplib
import urllib

class Test(object):
    def __init__(self, commands):
        self.__commands = commands
        self.__available_commands = {'address': (self.__is_ip_correct, ),
            'forward': (self.__is_speed_correct, self.__is_time_correct),
            'backward': (self.__is_speed_correct, self.__is_time_correct),
            'straight_left': (self.__is_speed_correct, self.__is_time_correct),
            'straight_right': (self.__is_speed_correct, self.__is_time_correct),
            'rotate_left_by_speed': (self.__is_speed_correct, ),
            'rotate_right_by_speed': (self.__is_speed_correct, ),
            'diagonal_forward_left': (self.__is_speed_correct,
                                      self.__is_time_correct),
            'diagonal_forward_right': (self.__is_speed_correct,
                                       self.__is_time_correct),
            'diagonal_backward_left': (self.__is_speed_correct,
                                       self.__is_time_correct),
            'diagonal_backward_right': (self.__is_speed_correct,
                                        self.__is_time_correct),
            'head_up': (self.__is_speed_correct, ),
            'head_down': (self.__is_speed_correct, ),
            'head_middle': (self.__is_speed_correct, ),
            'rotate_left_by_20_degree': (),
            'rotate_right_by_20_degree': (),
            'capture_image': ()
            }

    def syntax(self):
        line_number = 0

        for command in self.__commands:
            line_number += 1

            if line_number == 1:
                if command.get_name() != 'address':
                    print 'Syntax error\naddress should be first'
                    exit(-1)

            try:
                test_func = self.__available_commands[command.get_name()]
            except:
                print 'Syntax error\nline ' + str(line_number)
                exit(-1)

            params_count = len(command.get_params())

            if len(test_func) != params_count:
                print 'Syntax error\nline ' + str(line_number)
                exit(-1)

            for test, command in zip(test_func, command.get_params()):
                if not test(command):
                    print 'Syntax error\nline ' + str(line_number)
                    exit(-1)

        print 'Syntax test OK'

    def __is_speed_correct(self, speed):
        print speed
        return True

    def __is_time_correct(self, time):
        print time
        return True

    def ping(self):
        command = self.__commands.get(0)
        if command.get_name() != 'address':
            print 'Ping error\nFile syntax error\naddress keyword not found'
            exit(-1)

        ip = command.get_params()[0]
        if not self.__is_ip_correct(ip):
            print 'Ping error\nBad address'
            exit(-1)

        ping, battery = self.__request(ip)

        if not ping:
            exit(-1)

        print 'Ping test OK\nBattery level: ' + battery

    def __is_ip_correct(self, ip):
        print ip
        ip = ip.split('.')

        if len(ip) != 4:
            return False

        for i in ip:
            if int(i) < 0 or int(i) > 255:
                return False

        return True

    def __request(self, ip):
        connection = httplib.HTTPConnection(ip, timeout=10)

        params = urllib.urlencode([('Cmd', 'nav'), ('action', 1)])
        try:
            connection.request('POST','/cgi-bin/rev.cgi', params)
            response = connection.getresponse()
        except :
            print 'Ping error\nConnection failed'
            connection.close()
            return False, None

        response = response.read().strip('\n')
        connection.close()

        ping = response.split('\n')[1].split('|')[0].split('=')
        battery = response.split('\n')[7].split('|')[1].split('=')

        if int(ping[1]) == 0:
            return True, battery[1]
        else:
            return False, None
