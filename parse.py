"""
Copyright (C) 2019-2020 Zilliz. All rights reserved.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
     http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS S" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# pylint: disable=logging-format-interpolation

import logging
import getopt
import sys
import json

def usage():
    """
        help function
    """
    print('usage: python manange.py [options]')
    print('default: develop mode')
    print('-h: usage')
    print('--input_path=: path/to/input, default: ./')
    print('--output_path=: path/to/output, default: ./')

def parse_args(argv):
    input_path = "./"
    output_path = "./"
    try:
        OPTS, ARGS = getopt.getopt(argv[1:], 'h', ['input_path=', 'output_path='])
    except getopt.GetoptError as _e:
        print("Error '{}' occured. Arguments {}.".format(str(_e), _e.args))
        usage()
        sys.exit(2)

    for opt, arg in OPTS:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt == '--input_path':
            input_path = arg
        elif opt == '--output_path':
            output_path = arg

    return input_path, output_path