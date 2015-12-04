class Command(object):
    def __init__(self, command_array):
        self.__name = command_array[0]
        del command_array[0]
        self.__parameters = command_array

    def get_name(self):
        return self.__name

    def get_params(self):
        return self.__parameters


class Commands(object):
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
