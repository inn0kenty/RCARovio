import argparse

parser = argparse.ArgumentParser(description='Avaliable arguments')

parser.add_argument('-t', '--test', action='store_true',
                        help='Run syntactic test for input file')

parser.add_argument('-p', '--ping', action='store_true',
                        help='Ping rovio IP address')

parser.add_argument('-b', '--battery', action='store_true',
                        help='Show battery level')

parser.add_argument('file_path', metavar='FILE_NAME', type=str, nargs=1,
                        help='A path to file that contains a commands to Rovio')
