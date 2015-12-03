#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse


parser = argparse.ArgumentParser(description='Avaliable arguments')
parser.add_argument('-t', '--test', action='store_true',
                    help='Run syntactic test for input file')
parser.add_argument('-p', '--ping', action='store_true',
                    help='Ping rovio IP address')

parser.add_argument('file_path', metavar='FILE_NAME', type=str, nargs=1,
                    help='A path to file that contains a commands to Rovio')

def test():
    print 'test'

def ping():
    print 'ping'

def main():
    args = parser.parse_args()

    if args.ping:
        ping()
    if args.test:
        test()

    file_path = args.file_path[0]

if __name__ == '__main__':
    main()
