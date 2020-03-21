import unittest
from unittest import mock
import subprocess
import os

from vsg.tests import utils
from vsg.__main__ import read_configuration_files



class command_line_args():
    ''' This is used as an input into the read_configuration function.'''
    def __init__(self, configuration=False):
        self.configuration = configuration


class test_read_configuration_function(unittest.TestCase):

    def setUp(self):
        if os.path.isfile('deleteme.json'):
            os.remove('deleteme.json')

    def tearDown(self):
        if os.path.isfile('deleteme.json'):
            os.remove('deleteme.json')

    def test_file_list(self):
        oCommandLineArgs = command_line_args(['vsg/tests/vsg/read_configuration_files/config_w_file_list.json'])

        dExpected = {}
        dExpected['file_list'] = []
        dExpected['file_list'].append('vsg/tests/vsg/read_configuration_files/entity.vhd')
        dExpected['file_list'].append('vsg/tests/vsg/read_configuration_files/arch.vhd')
        dExpected['file_list'].append('vsg/tests/vsg/read_configuration_files/package.vhd')

        dActual = read_configuration_files(oCommandLineArgs)

        self.assertDictEqual(dActual, dExpected)


    def test_globbing_files(self):
        oCommandLineArgs = command_line_args(['vsg/tests/vsg/read_configuration_files/config_w_file_globbing.json'])

        dExpected = {}
        dExpected['file_list'] = []
        dExpected['file_list'].append('vsg/tests/vsg/read_configuration_files/package.vhd')
        dExpected['file_list'].append('vsg/tests/vsg/read_configuration_files/entity_2.vhd')
        dExpected['file_list'].append('vsg/tests/vsg/read_configuration_files/arch_2.vhd')
        dExpected['file_list'].append('vsg/tests/vsg/read_configuration_files/package_2.vhd')
        dExpected['file_list'].append('vsg/tests/vsg/read_configuration_files/arch.vhd')
        dExpected['file_list'].append('vsg/tests/vsg/read_configuration_files/entity.vhd')

        dActual = read_configuration_files(oCommandLineArgs)

        self.assertDictEqual(dActual, dExpected)

    def test_file_list_with_individual_rule_config(self):
        self.maxDiff = None
        oCommandLineArgs = command_line_args(['vsg/tests/vsg/read_configuration_files/config_w_file_list_w_individual_rule_config.json'])

        dExpected = {}
        dExpected['file_list'] = []
        dExpected['file_list'].append('vsg/tests/vsg/read_configuration_files/entity.vhd')
        dFile = {}
        dFile['vsg/tests/vsg/read_configuration_files/arch.vhd'] = {}
        dFile['vsg/tests/vsg/read_configuration_files/arch.vhd']['rule'] = {}
        dFile['vsg/tests/vsg/read_configuration_files/arch.vhd']['rule']['rule_001'] = {}
        dFile['vsg/tests/vsg/read_configuration_files/arch.vhd']['rule']['rule_001']['disable'] = True
        dExpected['file_list'].append(dFile)
        dExpected['file_list'].append('vsg/tests/vsg/read_configuration_files/package.vhd')

        dActual = read_configuration_files(oCommandLineArgs)

        self.assertDictEqual(dActual, dExpected)

    def test_file_list_globbing_with_individual_rule_config(self):
        self.maxDiff = None
        oCommandLineArgs = command_line_args(['vsg/tests/vsg/read_configuration_files/config_w_file_list_globbing_w_individual_rule_config.json'])

        dExpected = {}
        dExpected['file_list'] = []
        dExpected['file_list'].append('vsg/tests/vsg/read_configuration_files/entity.vhd')
        dFile = {}
        dFile['vsg/tests/vsg/read_configuration_files/arch_2.vhd'] = {}
        dFile['vsg/tests/vsg/read_configuration_files/arch_2.vhd']['rule'] = {}
        dFile['vsg/tests/vsg/read_configuration_files/arch_2.vhd']['rule']['rule_001'] = {}
        dFile['vsg/tests/vsg/read_configuration_files/arch_2.vhd']['rule']['rule_001']['disable'] = True
        dExpected['file_list'].append(dFile)
        dFile = {}
        dFile['vsg/tests/vsg/read_configuration_files/arch.vhd'] = {}
        dFile['vsg/tests/vsg/read_configuration_files/arch.vhd']['rule'] = {}
        dFile['vsg/tests/vsg/read_configuration_files/arch.vhd']['rule']['rule_001'] = {}
        dFile['vsg/tests/vsg/read_configuration_files/arch.vhd']['rule']['rule_001']['disable'] = True
        dExpected['file_list'].append(dFile)
        dFile = {}
        dFile['vsg/tests/vsg/read_configuration_files/package.vhd'] = {}
        dFile['vsg/tests/vsg/read_configuration_files/package.vhd']['rule'] = {}
        dFile['vsg/tests/vsg/read_configuration_files/package.vhd']['rule']['rule_002'] = {}
        dFile['vsg/tests/vsg/read_configuration_files/package.vhd']['rule']['rule_002']['disable'] = False
        dExpected['file_list'].append(dFile)

        dActual = read_configuration_files(oCommandLineArgs)

        self.assertDictEqual(dActual, dExpected)
