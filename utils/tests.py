from http import HTTPRequests


class Test(object):
    def __init__(self, address, commands):
        self.__address = address
        self.__commands = commands  # commands from file
        # all available commands
        self.__available_commands = {'forward': (self.__is_time_correct,),
                                     'backward': (self.__is_time_correct,),
                                     'straight_left': (self.__is_time_correct,),
                                     'straight_right': (self.__is_time_correct,),
                                     'rotate_left_by_speed':
                                     (self.__is_speed_correct,),
                                     'rotate_right_by_speed':
                                     (self.__is_speed_correct,),
                                     'diagonal_forward_left':
                                     (self.__is_time_correct,),
                                     'diagonal_forward_right':
                                     (self.__is_time_correct,),
                                     'diagonal_backward_left':
                                     (self.__is_time_correct,),
                                     'diagonal_backward_right':
                                     (self.__is_time_correct,),
                                     'head_up': (),
                                     'head_down': (),
                                     'head_middle':(),
                                     'rotate_left_by_20_degree': (),
                                     'rotate_right_by_20_degree': (),
                                     'capture_image': (),
                                     'wait': (self.__is_time_correct,),}

    def syntax(self):
        line_number = 0  # line counter

        if self.__address[0] != 'address' or not self.__is_ip_correct(
                self.__address[1]):
            print 'Syntax error\naddress should be first'
            return False

        for command in self.__commands:  # for all commands check parameters
            line_number += 1

            # checking if command is available
            try:
                test_func = self.__available_commands[command.get_name()]
            except:
                print 'Syntax error\nline ' + str(line_number)
                return False

            params_count = len(command.get_params())

            # if count of test functions not equal count of parameters then
            # it is error
            if len(test_func) != params_count:
                print 'Syntax error\nline ' + str(line_number)
                return False

            # checking all parameters the correctness
            for test, command in zip(test_func, command.get_params()):
                if not test(command):
                    print 'Syntax error\nline ' + str(line_number)
                    return False

        print 'Syntax test OK'
        return True

    def __is_speed_correct(self, speed):
        speed = int(speed)

        if (speed <= 0) or (speed > 10):
            return False

        return True

    def __is_time_correct(self, time):
        time = int(time)

        if time <= 0:
            return False

        return True

    def ping(self):
        # command = self.__commands.get(0)
        # checking if first command is a address
        if self.__address[0] != 'address':
            print 'Ping error\nFile syntax error\naddress keyword not found'
            return False

        # checking ip address the correctness
        ip = self.__address[1]
        if not self.__is_ip_correct(ip):
            print 'Ping error\nBad address'
            return False

        # send request to rovio
        with HTTPRequests(ip) as con:
            ping, battery = con.ping()

        if not ping:
            return False

        print 'Ping test OK\nBattery level: ' + battery
        return True

    def __is_ip_correct(self, ip):
        ip = ip.split('.')

        if len(ip) != 4:
            return False

        for i in ip:
            if int(i) < 0 or int(i) > 255:
                return False

        return True
