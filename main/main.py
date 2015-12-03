from roviotest import tests
from . import parser
import sys

def main():
    args = parser.parse_args()
    file_path = args.file_path[0]

    if len(sys.argv) > 2:
        test = tests.Test(file_path)
        if args.ping:
            test.ping()
        if args.test:
            test.syntax()

