class Command(object):
    def __init__(self, command_array):
        self.__name = command_array[0]
        del command_array[0]
        self.__parameters = command_array

    def get_name(self):
        return self.__name

    def get_params(self):
        return self.__parameters

#class FileParser(object):
#    def __init__(self, file_path):
#        self.__file_path = file_path

