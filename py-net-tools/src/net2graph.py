#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <martin.groenholdt@gmail.com> wrote this file. As long as you retain this notice
# you can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return. Martin B. K. Grønholdt
# --------------------------------------------------------------------------------
# Program to convert a database diagram written in a subset of PlantUML to
# SQLite syntax that will create the actual tables and relations.
#
# Version 0.0.1
#  * Initial code.
#
"""
Name: net2graph.py
Author: Martin Bo Kristensen Grønholdt.

Convert network information from YAML into a diagram.
"""
import argparse
import sys
from pprint import pprint
from argparse import ArgumentParser
from dotgen.dotgenerator import DotGenerator
from dotgen.exceptions import NoRendererException

from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

# Program version.
__VERSION__ = '0.0.1'


def parse_commandline():
    """
    Parse command line arguments.

    :return: A tuple with a list of files path to include, and a list of paths
             to exclude.
    """
    # Set up the arguments.
    parser = ArgumentParser(description='net2graph v{}'.format(__VERSION__) +
                                        ' by Martin B. K. Grønholdt\n' +
                                        'Convert network information from ' +
                                        'YAML into a diagram.')
    parser.add_argument('infile', type=argparse.FileType('r'),
                        help='YAML file with network information.')
    parser.add_argument('outfile', type=argparse.FileType('w'),
                        help='GrahViz style network diagram.', default=sys.stdout, nargs='?')

    # Parse command line
    args = parser.parse_args()

    # Return the paths.
    return ((args.infile, args.outfile))


def main():
    """
    Program main entry point.
    """
    # Parse the command line.
    (yaml_file, dot_file) = parse_commandline()

    dict_network = load(yaml_file, Loader=Loader)
    pprint(dict_network)

    try:
        dot_network = DotGenerator()
        dot_network.fromDict(dict_network)
        print()
        print(str(dot_network))
    except NoRendererException as nre:
        print(' No device renderer {}'.format(str(nre)))
        return 1

    return 0



# Run this when invoked directly
if __name__ == '__main__':
    sys.exit(main())
