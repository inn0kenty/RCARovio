import argparse
import shutil
import os


class CleanAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        path = os.getenv('HOME') + '/.rovio/'
        if os.path.exists(path):
            shutil.rmtree(path)
        parser.exit()


parser = argparse.ArgumentParser(description='Avaliable arguments')

parser.add_argument('-t', '--test', action='store_true',
                    help='Run syntactic test for input file')

parser.add_argument('-p', '--ping', action='store_true',
                    help='Ping rovio IP address')

parser.add_argument('-c', '--clean', action=CleanAction, nargs=0,
                    help='Cleans all stored images')

parser.add_argument('file_path', metavar='FILE_NAME', type=str, nargs=1,
                    help='A path to file that contains a commands to Rovio')
