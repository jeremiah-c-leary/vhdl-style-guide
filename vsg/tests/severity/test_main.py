
import shutil
import sys
import os


import unittest
from unittest import mock

from vsg import __main__
from vsg.tests import utils

sEntityFileName = 'entity.vhd'
sArchitectureFileName = 'architecture.vhd'
sJUnitFileName = 'junit_output.xml'

sEntityFile = os.path.join(os.path.dirname(__file__), sEntityFileName)
sArchitectureFile = os.path.join(os.path.dirname(__file__), sArchitectureFileName)
sJUnitFile = os.path.join(os.path.dirname(__file__), sJUnitFileName)
sConfigFile = os.path.join(os.path.dirname(__file__),'config.yaml')
sOutputFileWoConfig = os.path.join(os.path.dirname(__file__),'output_wo_config.txt')
sOutputFileWithConfig = os.path.join(os.path.dirname(__file__),'output_w_config.txt')
sOutputFileWithConfigFixed = os.path.join(os.path.dirname(__file__),'output_w_config_fixed.txt')
sArchitectureOutputFileWoConfig = os.path.join(os.path.dirname(__file__),'output_wo_config.architecture.txt')
sArchitectureOutputFileWithConfig = os.path.join(os.path.dirname(__file__),'output_w_config.architecture.txt')
sArchitectureOutputFileWithConfigFixed = os.path.join(os.path.dirname(__file__),'output_w_config_fixed.architecture.txt')

class test_severity_using_main(unittest.TestCase):

    def setUp(self):
        if os.path.isfile(sEntityFileName):
            os.remove(sEntityFileName)
        if os.path.isfile(sArchitectureFileName):
            os.remove(sArchitectureFileName)
        if os.path.isfile(sJUnitFileName):
            os.remove(sJUnitFileName)
        shutil.copyfile(sEntityFile, sEntityFileName)
        shutil.copyfile(sArchitectureFile, sArchitectureFileName)
        shutil.copyfile(sJUnitFile, sJUnitFileName)

    def tearDown(self):
        os.remove(sEntityFileName)
        os.remove(sArchitectureFileName)
        os.remove(sJUnitFileName)

    @mock.patch('sys.stdout')
    @mock.patch('vsg.__main__.rule_list.rule_list.get_number_of_rules_ran')
    def test_entity_without_configuration(self, mock_rule_ran, mock_stdout):
        mock_rule_ran.return_value = 200
        try:
            sys.argv =  ['vsg', '-f', sEntityFileName]
            __main__.main()
        except SystemExit as e:
            self.assertEqual(e.code, 1)

        lOutputFile = []
        utils.read_file(sOutputFileWoConfig, lOutputFile)

        lExpected = []
        for sLine in lOutputFile:
            lExpected.append(mock.call(sLine))
            lExpected.append(mock.call('\n'))

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch('sys.stdout')
    @mock.patch('vsg.__main__.rule_list.rule_list.get_number_of_rules_ran')
    def test_entity_with_configuration(self, mock_rule_ran, mock_stdout):
        mock_rule_ran.return_value = 200
        try:
            sys.argv =  ['vsg', '-f', sEntityFileName, '-c', sConfigFile]
            __main__.main()
        except SystemExit as e:
            self.assertEqual(e.code, 1)

        lOutputFile = []
        utils.read_file(sOutputFileWithConfig, lOutputFile)

        lExpected = []
        for sLine in lOutputFile:
            lExpected.append(mock.call(sLine))
            lExpected.append(mock.call('\n'))

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch('sys.stdout')
    @mock.patch('vsg.__main__.rule_list.rule_list.get_number_of_rules_ran')
    def test_entity_with_configuration_and_fixed(self, mock_rule_ran, mock_stdout):
        mock_rule_ran.return_value = 200
        try:
            sys.argv =  ['vsg', '-f', sEntityFileName, '-c', sConfigFile, '--fix']
            __main__.main()
        except SystemExit as e:
            self.assertEqual(e.code, 0)

        lOutputFile = []
        utils.read_file(sOutputFileWithConfigFixed, lOutputFile)

        lExpected = []
        for sLine in lOutputFile:
            lExpected.append(mock.call(sLine))
            lExpected.append(mock.call('\n'))

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch('sys.stdout')
    @mock.patch('vsg.__main__.rule_list.rule_list.get_number_of_rules_ran')
    def test_architecture_without_configuration(self, mock_rule_ran, mock_stdout):
        mock_rule_ran.return_value = 200
        try:
            sys.argv =  ['vsg', '-f', sArchitectureFileName]
            __main__.main()
        except SystemExit as e:
            self.assertEqual(e.code, 1)

        lOutputFile = []
        utils.read_file(sArchitectureOutputFileWoConfig, lOutputFile)

        lExpected = []
        for sLine in lOutputFile:
            lExpected.append(mock.call(sLine))
            lExpected.append(mock.call('\n'))

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch('sys.stdout')
    @mock.patch('vsg.__main__.rule_list.rule_list.get_number_of_rules_ran')
    def test_architecture_with_configuration(self, mock_rule_ran, mock_stdout):
        mock_rule_ran.return_value = 200
        try:
            sys.argv =  ['vsg', '-f', sArchitectureFileName, '-c', sConfigFile]
            __main__.main()
        except SystemExit as e:
            self.assertEqual(e.code, 1)

        lOutputFile = []
        utils.read_file(sArchitectureOutputFileWithConfig, lOutputFile)

        lExpected = []
        for sLine in lOutputFile:
            lExpected.append(mock.call(sLine))
            lExpected.append(mock.call('\n'))

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch('sys.stdout')
    @mock.patch('vsg.__main__.rule_list.rule_list.get_number_of_rules_ran')
    def test_architecture_with_configuration_and_fixed(self, mock_rule_ran, mock_stdout):
        mock_rule_ran.return_value = 200
        try:
            sys.argv =  ['vsg', '-f', sArchitectureFileName, '-c', sConfigFile, '--fix']
            __main__.main()
        except SystemExit as e:
            self.assertEqual(e.code, 0)

        lOutputFile = []
        utils.read_file(sArchitectureOutputFileWithConfigFixed, lOutputFile)

        lExpected = []
        for sLine in lOutputFile:
            lExpected.append(mock.call(sLine))
            lExpected.append(mock.call('\n'))

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch('sys.stdout')
    @mock.patch('vsg.__main__.rule_list.rule_list.get_number_of_rules_ran')
    def test_both_with_configuration(self, mock_rule_ran, mock_stdout):
        mock_rule_ran.return_value = 200
        try:
            sys.argv =  ['vsg', '-f', sEntityFileName, sArchitectureFileName, '-c', sConfigFile]
            __main__.main()
        except SystemExit as e:
            self.assertEqual(e.code, 1)


        lOutputFile = []
        utils.read_file(sOutputFileWithConfig, lOutputFile)
        utils.read_file(sArchitectureOutputFileWithConfig, lOutputFile)

        lExpected = []
        for sLine in lOutputFile:
            lExpected.append(mock.call(sLine))
            lExpected.append(mock.call('\n'))

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch('sys.stdout')
    @mock.patch('vsg.__main__.rule_list.rule_list.get_number_of_rules_ran')
    def test_both_with_configuration_and_fixed(self, mock_rule_ran, mock_stdout):
        mock_rule_ran.return_value = 200
        try:
            sys.argv =  ['vsg', '-f', sEntityFileName, sArchitectureFileName, '-c', sConfigFile, '--fix']
            __main__.main()
        except SystemExit as e:
            self.assertEqual(e.code, 0)


        lOutputFile = []
        utils.read_file(sOutputFileWithConfigFixed, lOutputFile)
        utils.read_file(sArchitectureOutputFileWithConfigFixed, lOutputFile)

        lExpected = []
        for sLine in lOutputFile:
            lExpected.append(mock.call(sLine))
            lExpected.append(mock.call('\n'))

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch('sys.stdout')
    def test_oc_option(self, mock_stdout):
        try:
            sys.argv =  ['vsg', '-oc', 'blah.json']
            __main__.main()
        except SystemExit as e:
            self.assertEqual(e.code, 0)

        lExpected = []

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch('sys.stdout')
    def test_junit_output(self,mock_stdout):
        try:
            sys.argv =  ['vsg', '-f', sEntityFileName, '-c', sConfigFile, '-j', sJUnitFileName]
            __main__.main()
        except SystemExit as e:
            self.assertEqual(e.code, 1)


        lActual = []
        utils.read_file(sJUnitFileName, lActual)

        lExpected = []
        utils.read_file(sJUnitFile, lExpected)

        self.assertEqual(len(lActual), len(lExpected))

        for iIndex, sLine in enumerate(lExpected):
            if not iIndex == 1:
                self.assertEqual(lActual[iIndex], sLine)
