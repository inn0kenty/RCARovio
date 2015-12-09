from command import CommandQueue


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

    def get_data(self) :
        return self.__address, self.__commands

    def __parse_command(self, command):
        command = command.strip('\n')
        command = (' '.join(command.split())).split(' ')
        return command
