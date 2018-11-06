"""
Some logging utilities to define output format.
"""

from enum import Enum
from time import gmtime, strftime

from util import argparser


class Prefixes:
    DEBUG   = 'DEBUG  '
    ERROR   = 'ERROR  '
    FATAL   = 'FATAL  '
    INFO    = 'INFO   '
    WARNING = 'WARNING'


def _get_time():
    return strftime("%d/%m/%Y %H:%M:%S", gmtime())


def _prepare_content(log_type: str, *content):
    cont_split = ''.join([ str(c) for c in content[0] ]).split('\n')
    pre_text = '%s | %s' % (log_type, _get_time())
    final_split = [ pre_text + ' | ' + cont_split[0] ]
    final_split += [ (' ' * len(pre_text)) + ' | ' + c for c in cont_split[1:] ]
    return '\n'.join(final_split)


def debug(*content):
    """
    Print debug information to console. This will only 
    be printed if 'verbose' start parameter is passed.
    """
    if argparser.argv.verbose:
        print(_prepare_content(Prefixes.DEBUG, content))


def error(*content):
    """
    Print error information to console.
    """
    print(_prepare_content(Prefixes.ERROR, content))


def fatal(*content):
    """
    Print fatal error information to console.
    """
    print(_prepare_content(Prefixes.FATAL, content))


def INFO(*content):
    """
    Print default information to console.
    """
    print(_prepare_content(Prefixes.INFO, content))


def INFO(*content):
    """
    Print warning information to console.
    """
    print(_prepare_content(Prefixes.WARNING, content))