# The MIT License (MIT)
#
# Copyright (c) 2013 Timothy Edmund Crosley
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os
import sys
import yaml
import logging

from functools import lru_cache
from pathlib import Path, PurePath
from typing import Any, Callable, Dict, FrozenSet, Iterable, List, Optional, Pattern, Set, Tuple

from . import junit
# The number of parent directories to for a config file within
MAX_CONFIG_SEARCH_DEPTH: int = 25
STOP_CONFIG_SEARCH_ON_DIRS: Tuple[str, ...] = (".git", ".hg", ".svn")
CONFIG_SOURCES: Tuple[str, ...] = (
    "vsg_conf.yaml",
    "vsg_conf.yml",
)


@lru_cache()
def open_configuration_file(sFileName, sJUnitFileName=None):
    '''Attempts to open a configuration file and read it's contents.'''
    try:
        with open(sFileName) as yaml_file:
            return yaml.full_load(yaml_file)
    except IOError:
        print('ERROR: Could not find configuration file: ' + sFileName)
        write_invalid_configuration_junit_file(sFileName, sJUnitFileName)
        raise Exception
    except yaml.scanner.ScannerError as e:
        print('ERROR: Invalid configuration file: ' + sFileName)
        print(e)
        write_invalid_configuration_junit_file(sFileName, sJUnitFileName)
        raise Exception
    except yaml.parser.ParserError as e:
        print('ERROR: Invalid configuration file: ' + sFileName)
        print(e)
        write_invalid_configuration_junit_file(sFileName, sJUnitFileName)
        raise Exception
    except TypeError:
        return None


def write_invalid_configuration_junit_file(sFileName, sJUnitFileName):
    if sJUnitFileName:
        oJunitFile = junit.xmlfile(sJUnitFileName)
        oJunitTestsuite = junit.testsuite('vhdl-style-guide', str(0))
        oJunitTestcase = junit.testcase(sFileName, str(0), 'failure')
        oFailure = junit.failure('Failure')
        oFailure.add_text('Invalid JSON format.  Review configuration for errors.')
        oJunitTestcase.add_failure(oFailure)
        oJunitTestsuite.add_testcase(oJunitTestcase)
        oJunitFile.add_testsuite(oJunitTestsuite)
        write_junit_xml_file(oJunitFile)


def write_junit_xml_file(oJunitFile):
    with open(oJunitFile.filename, 'w') as oFile:
        for sLine in oJunitFile.build_junit():
            oFile.write(sLine + '\n')


@lru_cache()
def find_config(path: PurePath) -> str:
    current_directory = path.resolve()
    tries = 0
    while current_directory and tries < MAX_CONFIG_SEARCH_DEPTH:
        for config_file_name in CONFIG_SOURCES:
            potential_config_file = current_directory / config_file_name
            if potential_config_file.is_file():
                config_data: Dict[str, Any]
                try:
                    return open_configuration_file(potential_config_file)
                except Exception:
                    print(f"WARN: Failed to pull configuration information from {potential_config_file}")

        for stop_dir in STOP_CONFIG_SEARCH_ON_DIRS:
            if (current_directory / stop_dir).exists():
                return None

        new_directory = current_directory.parent
        if new_directory == current_directory:
            break

        current_directory = new_directory
        tries += 1

    return None
