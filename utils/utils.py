class Command(object):
    def __init__(self, command_array):
        self.__name = command_array[0]
        del command_array[0]
        self.__parameters = command_array

    def get_name(self):
        return self.__name

    def get_params(self):
        return self.__parameters


class Commaands(object):
    def __init__(self):
        self.__commands = []

    def add_command(self, command):
        """ command should be as list """
        self.__commands.append(Command(command))

    def __iter__(self):
        self.__position = 0
        return self

    def next(self):
        if self.__position < len(self.__commands):
            return self.__commands[self.__position]
        else:
            raise StopIteration()



#class FileParser(object):
#    def __init__(self, file_path):
#        self.__file_path = file_path

