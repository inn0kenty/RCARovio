from roviotest import tests
from . import parser

def main():
    args = parser.parse_args()

    test = tests.Test()

    if args.ping:
        test.ping()
    if args.test:
        test.syntax()

    file_path = args.file_path[0]
