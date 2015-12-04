import httplib
import urllib

class Test(object):
    #__available_commands = {'address': }

    def __init__(self, file_path):
        self.__file_path = file_path
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
        command_file = open(self.__file_path, 'r')
        line_number = 0

        for line in command_file:
            line_number += 1
            commands = line.split(' ')

            for co in commands:
                if co == '' or co == '\n':
                    del commands[co]

            #del commands[len(commands) - 1] # remove \n from end
            print commands
            methods = self.__available_commands[commands[0]]
            del commands[0]

            #print methods[0](commands[0])

            if len(commands) != 0:
                if len(methods) != len(commands):
                    print methods, commands
                    print 'Syntax error\nline ' + str(line_number)
                    exit(-1)

                for method, command in zip(methods, commands):
                    method(command)

        command_file.close()

    def __is_speed_correct(self, speed):
        print 'speed'
        return True

    def __is_time_correct(self, time):
        print 'time'
        return True

    def  ping(self):
        command_file = open(self.__file_path, 'r')
        command = command_file.readline().strip('\n')
        command_file.close()
        command = command.split(' ')
        #print self.__available_commands[command[0]](command[1])

        #if not (command[0] in Test.__available_commands):
        #    print 'Ping error\nFile syntax error\naddress keyword not found'
        #    exit(-1)

        if not self.__available_commands[command[0]](command[1]):
            print 'Ping error\nFile syntax error\naddress keyword not found or\
                \nip is incorrect'
            exit(-1)

        ping, battery = self.__request(command[1])

        if not ping:
            exit(-1)

        print 'Ping test OK\nBattery lavel: ' + battery

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

        params = urllib.urlencode([('Cmd', 'nav'), ('action', 1)])
        try:
            connection.request('POST','/rev.cgi', params)
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
