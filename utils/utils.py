from command import CommandQueue
import os


class FileParser(object):
    """Parse commands from file to a CommandQueue object"""
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__commands = CommandQueue()

        command_file = open(file_path, 'r')
        self.__address = self.__parse_command(command_file.readline())

        for command in command_file:
            if command != '\n':
                self.__commands.add_command(self.__parse_command(command))

    def get_data(self):
        return self.__address, self.__commands

    def __parse_command(self, command):
        command = command.strip('\n')
        command = (' '.join(command.split())).split(' ')
        return command


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(
                *args, **kwargs)

        return cls._instances[cls]


class Config(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.__parameters = {}
        for loc in os.path.abspath(os.curdir), '/etc/rovio':
            try:
                with open(os.path.join(loc, 'rovio.cfg')) as source:
                    for param in source:
                        key, value = self.__parse_param(param)
                        self.__parameters[key] = value
            except IOError:
                pass

    def get(self, name):
        if name == 'open':
            return self.__parameters.get(name, 'open')
        elif name == 'resolution':
            return self.__parameters.get(name, '3')

    def __parse_param(self, param):
        param = param.strip('\n')
        param = (''.join(param.split())).split(':')
        return param


