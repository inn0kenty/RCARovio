class Command(object):
    """The Command class represent a one instruction to rovio"""
    def __init__(self, command_array):
        self.__name = command_array[0]  # command name
        self.__value = self.__set_value(self.__name)
        del command_array[0]
        command_array = dict(enumerate(command_array))
        self.__speed = command_array.get(0, 1)
        self.__time = command_array.get(1, 1)
        #self.__parameters = command_array  # parameters for command

    def get_name(self):
        return self.__name

    def get_speed(self):
        return self.__speed

    def get_time(self):
        return self.__time

    def get_value(self):
        return self.__value

    def __set_value(self, x):
        return { 'address': 0,
                'forward': 1,
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
                'capture_image': 19
                }.get(x, -1)

class Commands(object):
    """The Commands class represent a list of commands that rovio should do"""
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


class FileParser(object):
    """Parse commands from file to a Commands object"""
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__commands = Commands()

        command_file = open(file_path, 'r')
        for command in command_file:
            if command != '\n':
                self.__commands.add_command(self.__parse_command(command))

    def get_commands(self):
        return self.__commands

    def __parse_command(self, command):
        command = command.strip('\n')
        command = (' '.join(command.split())).split(' ')
        return command
