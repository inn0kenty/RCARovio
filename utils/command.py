class Command(object):
    """The Command class represent a one instruction to rovio"""
    def __init__(self, command_array):
        self.__name = command_array[0]  # command name
        self.__value = self.__set_value(self.__name)

        del command_array[0]

        self.__parameters = command_array
        command_array = dict(enumerate(command_array))
        self.__speed = 1 #command_array.get(0, 10)
        self.__time = command_array.get(0, -1)

    def get_name(self):
        return self.__name

    def get_speed(self):
        return self.__speed

    def get_time(self):
        return int(self.__time)

    def get_value(self):
        return self.__value

    def get_params(self):
        return self.__parameters

    def __set_value(self, x):
        return {'forward': 1,
                'backward': 2,
                'straight_left': 3,
                'straight_right': 4,
                'rotate_left_by_speed': 5,
                'rotate_right_by_speed': 6,
                'diagonal_forward_left': 7,
                'diagonal_forward_right': 8,
                'diagonal_backward_left': 9,
                'diagonal_backward_right': 10,
                'head_up': 11,
                'head_down': 12,
                'head_middle': 13,
                'rotate_left_by_20_degree': 17,
                'rotate_right_by_20_degree': 18,
                'capture_image': 19,
                'wait': 20,
                }.get(x, -1)

class CommandQueue(object):
    """The CommandQueue class represent a queue of
    commands that rovio should do"""
    def __init__(self):
        self.__commands = []

    def add_command(self, command):
        """ command should be as list """
        self.__commands.append(Command(command))

    def get(self, index):
        if (0 <= index) and (index < len(self.__commands)):
            return self.__commands[index]
        else:
            return None

    def __iter__(self):
        self.__position = -1
        return self

    def next(self):
        if self.__position < len(self.__commands) - 1:
            self.__position += 1
            return self.__commands[self.__position]
        else:
            raise StopIteration()

