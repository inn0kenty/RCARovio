from test import tests
from . import parser
import sys
import os.path
from utils import utils

def main():
    args = parser.parse_args()
    file_path = args.file_path[0]

    if not os.path.isfile(file_path):
        print 'File not found'
        exit(-1);

    file_parser = utils.FileParser(file_path)
    address, commands = file_parser.get_data()

    if len(sys.argv) > 2:
        test = tests.Test(address, commands)
        if args.ping:
            test.ping()
        if args.test:
            test.syntax()

