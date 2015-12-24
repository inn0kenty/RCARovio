from utils.tests import Test
from . import parser
import sys
import os.path
from utils.utils import FileParser, Config
from rovio_base.rovio import Rovio

def main() :
    args = parser.parse_args()
    file_path = args.file_path[0]

    if not os.path.isfile(file_path):
        print 'File not found'
        exit(-1);

    file_parser = FileParser(file_path)
    address, commands = file_parser.get_data()
    config = Config()

    if len(sys.argv) > 2:
        test = Test(address, commands)
        if args.ping:
            test.ping()
        if args.test:
            test.syntax()
    else:
        remote_rovio = Rovio(address[1], commands)
        remote_rovio.do()
