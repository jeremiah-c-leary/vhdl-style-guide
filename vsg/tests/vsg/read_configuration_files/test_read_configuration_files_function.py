import unittest
import os

from vsg.config import read_configuration_files

def get_index_of_dictionary_in_list(lList, sKey):
    for iIndex, item in enumerate(lList):
        if isinstance(item, dict):
            sMyKey = list(item.keys())[0]
            if sMyKey == sKey:
                return iIndex
    return None


class command_line_args():
    ''' This is used as an input into the read_configuration function.'''
    def __init__(self, configuration=False):
        self.configuration = configuration
        self.junit = None


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
        dExpected['file_list'].append('vsg/tests/vsg/read_configuration_files/arch.vhd')
        dExpected['file_list'].append('vsg/tests/vsg/read_configuration_files/entity.vhd')
        dExpected['file_list'].append('vsg/tests/vsg/read_configuration_files/package.vhd')

        dActual = read_configuration_files({}, oCommandLineArgs)

        dExpected['file_list'].sort()
        dActual['file_list'].sort()

        self.assertDictEqual(dActual, dExpected)


    def test_globbing_files(self):
        oCommandLineArgs = command_line_args(['vsg/tests/vsg/read_configuration_files/config_w_file_globbing.json'])

        dExpected = {}
        dExpected['file_list'] = []
        dExpected['file_list'].append('vsg/tests/vsg/read_configuration_files/package.vhd')
        dExpected['file_list'].append('vsg/tests/vsg/read_configuration_files/entity_2.vhd')
        dExpected['file_list'].append('vsg/tests/vsg/read_configuration_files/arch_2.vhd')
        dExpected['file_list'].append('vsg/tests/vsg/read_configuration_files/arch.vhd')
        dExpected['file_list'].append('vsg/tests/vsg/read_configuration_files/package_2.vhd')
        dExpected['file_list'].append('vsg/tests/vsg/read_configuration_files/entity.vhd')

        dActual = read_configuration_files({}, oCommandLineArgs)

        dExpected['file_list'].sort()
        dActual['file_list'].sort()

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

        dActual = read_configuration_files({}, oCommandLineArgs)

        lExpected = []
        for item in dExpected['file_list']:
            if not isinstance(item, dict):
                lExpected.append(item)
        lExpected.sort()

        lActual = []
        for item in dActual['file_list']:
            if not isinstance(item, dict):
                lActual.append(item)
        lActual.sort()

        self.assertEqual(lActual, lExpected)

        for iIndex, item in enumerate(dExpected['file_list']):
            if isinstance(item, dict):
                sKey = list(item.keys())[0]
                iActualIndex = get_index_of_dictionary_in_list(dActual['file_list'], sKey)
                self.assertEqual(dActual['file_list'][iActualIndex], dExpected['file_list'][iIndex])


    def test_file_list_globbing_with_individual_rule_config(self):
        self.maxDiff = None
        oCommandLineArgs = command_line_args(['vsg/tests/vsg/read_configuration_files/config_w_file_list_globbing_w_individual_rule_config.json'])

        dExpected = {}
        dExpected['file_list'] = []

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

        dExpected['file_list'].append('vsg/tests/vsg/read_configuration_files/entity.vhd')

        dActual = read_configuration_files({}, oCommandLineArgs)

        lExpected = []
        for item in dExpected['file_list']:
            if not isinstance(item, dict):
                lExpected.append(item)
        lExpected.sort()

        lActual = []
        for item in dActual['file_list']:
            if not isinstance(item, dict):
                lActual.append(item)
        lActual.sort()

        self.assertEqual(lActual, lExpected)

        for iIndex, item in enumerate(dExpected['file_list']):
            if isinstance(item, dict):
                sKey = list(item.keys())[0]
                iActualIndex = get_index_of_dictionary_in_list(dActual['file_list'], sKey)
                self.assertEqual(dActual['file_list'][iActualIndex], dExpected['file_list'][iIndex])

