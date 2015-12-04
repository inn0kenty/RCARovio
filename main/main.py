from test import tests
from . import parser
import sys
import os.path

def main():
    args = parser.parse_args()
    file_path = args.file_path[0]

    if not os.path.isfile(file_path):
        print 'File not found'
        exit(-1);

    if len(sys.argv) > 2:
        test = tests.Test(file_path)
        if args.ping:
            test.ping()
        if args.test:
            test.syntax()
        if args.battery:
            test.battery()

