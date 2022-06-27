import filecmp
import pathlib
import unittest
from unittest import mock
import os
import subprocess
import shutil
import sys
import shutil

import contextlib
from io import StringIO

from tempfile import TemporaryFile

from vsg.tests import utils
from vsg import version
from vsg import __main__


class command_line_args():
    ''' This is used as an input into the version command.'''
    def __init__(self, version=False):
        self.version = version


class testMain(unittest.TestCase):

    def setUp(self):
        if os.path.isfile('deleteme.json'):
            os.remove('deleteme.json')

    def tearDown(self):
        if os.path.isfile('deleteme.json'):
            os.remove('deleteme.json')

    @mock.patch('sys.stdout')
    def test_multiple_configuration_w_multiple_filelists(self, mock_stdout):

        lExpected = []
        lExpected.append(mock.call('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.'))
        lExpected.append(mock.call('\n'))
        lExpected.append(mock.call('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.'))
        lExpected.append(mock.call('\n'))

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['--configuration', 'vsg/tests/vsg/config_1.json', 'vsg/tests/vsg/config_2.json'])
        sys.argv.extend(['-p 1'])

        try:
            __main__.main()
        except SystemExit:
            pass

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch('sys.stdout')
    def test_single_configuration_w_filelist(self, mock_stdout):
        lExpected = []
        lExpected.append(mock.call('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.'))
        lExpected.append(mock.call('\n'))

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['--configuration', 'vsg/tests/vsg/config_1.json'])
        sys.argv.extend(['-p 1'])

        try:
            __main__.main()
        except SystemExit:
            pass

        mock_stdout.write.assert_has_calls(lExpected)

        lExpected = []
        lExpected.append(mock.call('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.'))
        lExpected.append(mock.call('\n'))

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['--configuration', 'vsg/tests/vsg/config_2.json'])
        sys.argv.extend(['-p 1'])

        try:
            __main__.main()
        except SystemExit:
            pass

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch('sys.stdout')
    def test_single_configuration_w_rule_disable(self, mock_stdout):
        lExpected = []
        lExpected.append(mock.call('\n'))

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['--configuration', 'vsg/tests/vsg/config_3.json'])
        sys.argv.extend(['-p 1'])

        try:
            __main__.main()
        except SystemExit:
            pass

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch('sys.stdout')
    def test_multiple_configuration_w_rule_disable(self, mock_stdout):
        lExpected = []
        lExpected.append(mock.call('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.'))
        lExpected.append(mock.call('\n'))

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['--configuration', 'vsg/tests/vsg/config_3.json', 'vsg/tests/vsg/config_4.json'])
        sys.argv.extend(['-f', 'vsg/tests/vsg/entity1.vhd'])
        sys.argv.extend(['-p 1'])

        try:
            __main__.main()
        except SystemExit:
            pass

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch('sys.stdout')
    def test_invalid_configuration(self, mock_stdout):
#    def test_invalid_configuration(self):
        utils.remove_file('vsg/tests/vsg/config_error.actual.xml')
        lExpected = []
        lExpected.append(mock.call('ERROR: Invalid configuration file: vsg/tests/vsg/config_error.json'))
        lExpected.append(mock.call('\n'))
        lExpected.append(mock.call('while parsing a flow node\nexpected the node content, but found \',\'\n  in "vsg/tests/vsg/config_error.json", line 2, column 16'))
        lExpected.append(mock.call('\n'))

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['--configuration', 'vsg/tests/vsg/config_error.json'])
        sys.argv.extend(['-f', 'vsg/tests/vsg/entity1.vhd'])
        sys.argv.extend(['--junit', 'vsg/tests/vsg/config_error.actual.xml'])
        sys.argv.extend(['-p 1'])

        try:
            __main__.main()
        except SystemExit:
            pass

        mock_stdout.write.assert_has_calls(lExpected)

        # Read in the expected JUnit XML file for comparison
        lExpected = []
        utils.read_file(os.path.join(os.path.dirname(__file__),'config_error.expected.xml'), lExpected)
        # Read in the actual JUnit XML file for comparison
        lActual = []
        utils.read_file(os.path.join(os.path.dirname(__file__),'config_error.actual.xml'), lActual)
        # Compare the two files, but skip the line with the timestamp (as it will never match)
        for iLineNumber, sLine in enumerate(lExpected):
            if iLineNumber != 1:
                self.assertEqual(sLine, lActual[iLineNumber])
        # Clean up
        utils.remove_file('vsg/tests/vsg/config_error.actual.xml')

    @mock.patch('sys.stdout')
    def test_local_rules(self,mock_stdout):
        lExpected = []
        lExpected.append(mock.call('ERROR: vsg/tests/vsg/entity_architecture.vhd(1)localized_001 -- Split entity and architecture into seperate files.'))
        lExpected.append(mock.call('\n'))

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['--style', 'jcl'])
        sys.argv.extend(['-f', 'vsg/tests/vsg/entity_architecture.vhd'])
        sys.argv.extend(['-lr', 'vsg/tests/vsg/local_rules'])
        sys.argv.extend(['-p 1'])

        try:
            __main__.main()
        except SystemExit:
            pass

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch('sys.stdout')
    def test_invalid_local_rule_directory(self, mock_stdout):
        lExpected = []
        lExpected.append(mock.call('ERROR: encountered FileNotFoundError, No such file or directory vsg/tests/vsg/invalid_local_rule_directory when trying to open local rules file.'))
        lExpected.append(mock.call('\n'))

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['-f', 'vsg/tests/vsg/entity_architecture.vhd'])
        sys.argv.extend(['-lr', 'vsg/tests/vsg/invalid_local_rule_directory'])
        sys.argv.extend(['-p 1'])

        try:
            __main__.main()
        except SystemExit:
            pass

        mock_stdout.write.assert_has_calls(lExpected)

    def test_globbing_filenames_in_configuration(self):
        lExpected = []
        lExpected.append('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.')
        lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.')

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['--configuration', 'vsg/tests/vsg/config_glob.json'])
        sys.argv.extend(['-p 1'])

        temp_stdout = StringIO()

        with contextlib.redirect_stdout(temp_stdout):

            try:
                __main__.main()
            except SystemExit:
                pass

        lActual = temp_stdout.getvalue().strip().split('\n')

        if lActual[0] == lExpected[1]:
            lExpected = [lExpected[1], lExpected[0]]

        self.assertEqual(lExpected, lActual)

    @mock.patch('sys.stdout')
    def test_single_yaml_configuration_w_filelist(self, mock_stdout):
        lExpected = []
        lExpected.append(mock.call('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.'))
        lExpected.append(mock.call('\n'))

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['--configuration', 'vsg/tests/vsg/config_1.yaml'])
        sys.argv.extend(['-p 1'])

        try:
            __main__.main()
        except SystemExit:
            pass

        mock_stdout.write.assert_has_calls(lExpected)

        lExpected = []
        lExpected.append(mock.call('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.'))
        lExpected.append(mock.call('\n'))

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['--configuration', 'vsg/tests/vsg/config_2.json'])
        sys.argv.extend(['-p 1'])

        try:
            __main__.main()
        except SystemExit:
            pass

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch('sys.stdout')
    def test_multiple_yaml_configuration_w_multiple_filelists(self, mock_stdout):
        lExpected = []
        lExpected.append(mock.call('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.'))
        lExpected.append(mock.call('\n'))
        lExpected.append(mock.call('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.'))
        lExpected.append(mock.call('\n'))

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['--configuration', 'vsg/tests/vsg/config_1.yaml', 'vsg/tests/vsg/config_2.yaml'])
        sys.argv.extend(['-p 1'])

        try:
            __main__.main()
        except SystemExit:
            pass

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch('sys.stdout')
    def test_single_yaml_configuration_w_rule_disable(self, mock_stdout):
        lExpected = []

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['--configuration', 'vsg/tests/vsg/config_3.yaml'])
        sys.argv.extend(['-f', 'vsg/tests/vsg/entity1.vhd'])
        sys.argv.extend(['-p 1'])

        try:
            __main__.main()
        except SystemExit:
            pass

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch('sys.stdout')
    def test_multiple_yaml_configuration_w_rule_disable(self, mock_stdout):
        lExpected = []
        lExpected.append(mock.call('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.'))
        lExpected.append(mock.call('\n'))

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['--configuration', 'vsg/tests/vsg/config_3.yaml', 'vsg/tests/vsg/config_4.yaml'])
        sys.argv.extend(['-f', 'vsg/tests/vsg/entity1.vhd'])
        sys.argv.extend(['-p 1'])

        try:
            __main__.main()
        except SystemExit:
            pass

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch('sys.stdout')
    def test_reverse_yaml_multiple_configuration_w_rule_disable(self, mock_stdout):
        lExpected = []

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['--configuration', 'vsg/tests/vsg/config_4.yaml', 'vsg/tests/vsg/config_3.yaml'])
        sys.argv.extend(['-f', 'vsg/tests/vsg/entity1.vhd'])
        sys.argv.extend(['-p 1'])

        try:
            __main__.main()
        except SystemExit:
            pass

        mock_stdout.write.assert_has_calls(lExpected)

    def test_globbing_filenames_in_yaml_configuration(self):
        lExpected = []
        lExpected.append('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.')
        lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.')

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['--configuration', 'vsg/tests/vsg/config_glob.yaml'])
        sys.argv.extend(['-p 1'])

        temp_stdout = StringIO()

        with contextlib.redirect_stdout(temp_stdout):

            try:
                __main__.main()
            except SystemExit:
                pass

        lActual = temp_stdout.getvalue().strip().split('\n')

        if lActual[0] == lExpected[1]:
            lExpected = [lExpected[1], lExpected[0]]

        self.assertEqual(lExpected, lActual)

    @mock.patch('sys.stdout')
    def test_oc_command_line_argument(self, mock_stdout):
        lExpected = []

        sys.argv = ['vsg']
        sys.argv.extend(['-oc', 'deleteme.json'])
        sys.argv.extend(['-p 1'])

        try:
            __main__.main()
        except SystemExit:
            pass

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch('sys.stdout')
    def test_rule_disabled_under_file(self, mock_stdout):
        lExpected = []

        sys.argv = ['vsg']
        sys.argv.extend(['-c', 'vsg/tests/vsg/config_rule_disabled_under_file.yaml'])
        sys.argv.extend(['-p 1'])

        try:
            __main__.main()
        except SystemExit:
            pass

        mock_stdout.write.assert_has_calls(lExpected)

    @unittest.skip('disabling for the hotfix release only')
    def test_json_parameter(self):
        self.maxDiff = None

        self.assertFalse(os.path.isfile('deleteme.json'))

        lExpected = []
        lExpected.append('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.')
        lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.')

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['--configuration', 'vsg/tests/vsg/config_glob.yaml'])
        sys.argv.extend(['--json', 'deleteme.json'])
        sys.argv.extend(['-p 1'])

        temp_stdout = StringIO()

        with contextlib.redirect_stdout(temp_stdout):

            try:
                __main__.main()
            except SystemExit:
                pass

        self.assertTrue(os.path.isfile('deleteme.json'))

        # Read in the expected JSON file for comparison
        lExpected = []
        utils.read_file(os.path.join(os.path.dirname(__file__),'json-expected.json'), lExpected)
        # Read in the alternate expected JSON file for comparison
        lAlternateExpected = []
        utils.read_file(os.path.join(os.path.dirname(__file__),'json-expected.alternate.json'), lAlternateExpected)
        # Read in another alternate expected JSON file for comparison
        lAlternateExpected2 = []
        utils.read_file(os.path.join(os.path.dirname(__file__),'json-expected.alternate2.json'), lAlternateExpected2)
        # Read in another alternate expected JSON file for comparison
        lAlternateExpected3 = []
        utils.read_file(os.path.join(os.path.dirname(__file__),'json-expected.alternate3.json'), lAlternateExpected3)
        # Read in another alternate expected JSON file for comparison
        lAlternateExpected4 = []
        utils.read_file(os.path.join(os.path.dirname(__file__),'json-expected.alternate4.json'), lAlternateExpected4)
        # Read in another alternate expected JSON file for comparison
        lAlternateExpected5 = []
        utils.read_file(os.path.join(os.path.dirname(__file__),'json-expected.alternate5.json'), lAlternateExpected5)
        # Read in another alternate expected JSON file for comparison
        lAlternateExpected6 = []
        utils.read_file(os.path.join(os.path.dirname(__file__),'json-expected.alternate6.json'), lAlternateExpected6)
        # Read in another alternate expected JSON file for comparison
        lAlternateExpected7 = []
        utils.read_file(os.path.join(os.path.dirname(__file__),'json-expected.alternate7.json'), lAlternateExpected7)

        # Read in the actual JSON file for comparison
        lActual = []
        utils.read_file(os.path.join('deleteme.json'), lActual)

        self.assertEqual(len(lExpected), len(lActual))

        if lActual == lExpected:
            self.assertEqual(lActual, lExpected)
        elif lActual == lAlternateExpected:
            self.assertEqual(lActual, lAlternateExpected)
        elif lActual == lAlternateExpected2:
            self.assertEqual(lActual, lAlternateExpected2)
        elif lActual == lAlternateExpected3:
            self.assertEqual(lActual, lAlternateExpected3)
        elif lActual == lAlternateExpected4:
            self.assertEqual(lActual, lAlternateExpected4)
        elif lActual == lAlternateExpected5:
            self.assertEqual(lActual, lAlternateExpected5)
        elif lActual == lAlternateExpected6:
            self.assertEqual(lActual, lAlternateExpected6)
        elif lActual == lAlternateExpected7:
            self.assertEqual(lActual, lAlternateExpected7)
        else:
            self.assertEqual(lActual, lAlternateExpected6)

#        for sActual, sExpected in zip(lActual, lExpected):
#            self.assertEqual(sActual, sExpected)

    @mock.patch('sys.stdout')
    def test_backup_file(self, mock_stdout):

        if os.path.isfile('vsg/tests/vsg/deleteme.vhd'):
            os.remove('vsg/tests/vsg/deleteme.vhd')

        if os.path.isfile('vsg/tests/vsg/deleteme.vhd.bak'):
            os.remove('vsg/tests/vsg/deleteme.vhd.bak')

        shutil.copyfile('vsg/tests/vsg/entity1.vhd', 'vsg/tests/vsg/deleteme.vhd')

        lExpected = []

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['-f', 'vsg/tests/vsg/deleteme.vhd'])
        sys.argv.extend(['--fix'])
        sys.argv.extend(['--backup'])
        sys.argv.extend(['-p 1'])

        try:
            __main__.main()
        except SystemExit:
            pass

        self.assertTrue(os.path.isfile('vsg/tests/vsg/deleteme.vhd.bak'))

        self.assertTrue(filecmp.cmp('vsg/tests/vsg/entity1.vhd', 'vsg/tests/vsg/deleteme.vhd.bak'))

        mock_stdout.write.assert_has_calls(lExpected)

        if os.path.isfile('vsg/tests/vsg/deleteme.vhd'):
            os.remove('vsg/tests/vsg/deleteme.vhd')

        if os.path.isfile('vsg/tests/vsg/deleteme.vhd.bak'):
            os.remove('vsg/tests/vsg/deleteme.vhd.bak')

    @mock.patch('sys.stdout')
    def test_backup_file_without_fix(self, mock_stdout):

        lExpected = []
        lExpected.append(mock.call('ERROR:  --backup argument requires --fix argument'))
        lExpected.append(mock.call('\n'))

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['-f', 'vsg/tests/vsg/entity1.vhd'])
        sys.argv.extend(['--backup'])
        sys.argv.extend(['-p 1'])

        with self.assertRaises(SystemExit) as cm:
            __main__.main()

        mock_stdout.write.assert_has_calls(lExpected)
        self.assertEqual(cm.exception.code, 1)
        self.assertFalse(os.path.isfile('vsg/tests/vsg/entity1.vhd.bak'))

    @mock.patch('sys.stdout')
    def test_ap_with_fix(self, mock_stdout):

        lExpected = []
        lExpected.append(mock.call('ERROR:  -ap argument is invalid with the --fix argument'))
        lExpected.append(mock.call('\n'))

        sys.argv = ['vsg']
        sys.argv.extend(['--output_format', 'syntastic'])
        sys.argv.extend(['-f', 'vsg/tests/vsg/entity1.vhd'])
        sys.argv.extend(['-ap'])
        sys.argv.extend(['--fix'])
        sys.argv.extend(['-p 1'])

        with self.assertRaises(SystemExit) as cm:
            __main__.main()

        mock_stdout.write.assert_has_calls(lExpected)
        self.assertEqual(cm.exception.code, 1)

    @mock.patch('sys.stdout')
    def test_syntastic_output_with_multiple_errors(self, mock_stdout):

        sOutput = ''
        sOutput += 'ERROR: vsg/tests/vsg/syntastic/syntastic.vhd(2)architecture_004 -- Change "ARCHITECTURE" to "architecture"\n'
        sOutput += 'ERROR: vsg/tests/vsg/syntastic/syntastic.vhd(2)architecture_013 -- Change "RTL" to "rtl"\n'
        sOutput += 'ERROR: vsg/tests/vsg/syntastic/syntastic.vhd(2)architecture_014 -- Change "FIFO" to "fifo"\n'
        sOutput += 'ERROR: vsg/tests/vsg/syntastic/syntastic.vhd(2)architecture_019 -- Change "OF" to "of"\n'
        sOutput += 'ERROR: vsg/tests/vsg/syntastic/syntastic.vhd(2)architecture_020 -- Change "IS" to "is"\n'
        sOutput += 'ERROR: vsg/tests/vsg/syntastic/syntastic.vhd(4)architecture_021 -- Change "BEGIN" to "begin"\n'
        sOutput += 'ERROR: vsg/tests/vsg/syntastic/syntastic.vhd(6)architecture_009 -- Change "END" to "end"\n'
        sOutput += 'ERROR: vsg/tests/vsg/syntastic/syntastic.vhd(6)architecture_011 -- Change "RTL" to "rtl"\n'
        sOutput += 'ERROR: vsg/tests/vsg/syntastic/syntastic.vhd(6)architecture_028 -- Change "ARCHITECTURE" to "architecture"'

        lExpected = []
        lExpected.append(mock.call(sOutput))
        lExpected.append(mock.call('\n'))

        sys.argv = ['vsg', '-f', 'vsg/tests/vsg/syntastic/syntastic.vhd', '-of', 'syntastic', '-p', '1']

        try:
            __main__.main()
        except SystemExit:
            pass

        mock_stdout.write.assert_has_calls(lExpected)

