import argparse


argv = None

def init():
    global argv
    arg_parser = argparse.ArgumentParser(description='Interprete and execute Discord Script.')
    arg_parser.add_argument('commands', metavar='CMD', nargs='*')
    arg_parser.add_argument('--file', '-f', nargs=1, help='Read script from file and execute.')
    arg_parser.add_argument('--verbose', '-v', action='store_const', const=True, default=False, help='Set output mode to verbose.')
    argv = arg_parser.parse_args()