#!/usr/bin/env python3

"""
DiscordScript - beta v.0.1.0
© 2018 zekro Development
Licence: MIT
"""

import re
import os.path

import logging
import cmdparser
from util import logger, argparser
from commands import token


def _prepare_command_stack(command_chain: str):
    chain_split = command_chain.split('\n')
    command_chain = ' '.join([ c for c in chain_split if len(c.strip()) > 0 and not c.strip().startswith('#') ])
    pattern = re.compile(r'''((?:[^;"']|"[^"]*"|'[^']*')+)''')
    split = pattern.split(command_chain)[1::2]
    split_stripped = [ c.strip() for c in split ]
    return split_stripped


def main():
    argparser.init()
    logger.debug('Verbose mode enabled\nARGV: ', argparser.argv)

    command_stack = _prepare_command_stack(' '.join(argparser.argv.commands))

    if argparser.argv.file:
        file_name = argparser.argv.file[0]
        if not os.path.isfile(file_name):
            logger.fatal('File not found')
            exit(1)

        with open(file_name, 'r') as f_handler:
            command_stack = _prepare_command_stack(f_handler.read())

    logger.debug('COMMANDS: ', command_stack)

    cmd_parser = cmdparser.CommandParser()
    cmd_parser.register("TOKEN", token.Token)
    cmd_parser.parse_command_stack(command_stack)


if __name__ == '__main__':
    main()