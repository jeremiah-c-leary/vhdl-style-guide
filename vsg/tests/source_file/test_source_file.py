import os
import pathlib
import unittest
from unittest import mock
import sys
import subprocess
sys.path.append('vsg')

from vsg.rules import source_file
from vsg import vhdlFile
from vsg import __main__
from vsg.tests import utils

sNoPermissionFile = 'no_permission.vhd'
sEmptyFile = 'empty_file.vhd'

sOutputNoFile = os.path.join(os.path.dirname(__file__),'output_no_file.txt')
sOutputNoPermission = os.path.join(os.path.dirname(__file__),'output_no_permission.txt')
sOutputEmptyFile = os.path.join(os.path.dirname(__file__),'output_empty_file.txt')

class testOSError(unittest.TestCase):

    def tearDown(self):
        if os.path.isfile(sNoPermissionFile):
            os.remove(sNoPermissionFile)

    @mock.patch('sys.stdout')
    @mock.patch('vsg.__main__.rule_list.rule_list.get_number_of_rules_ran')
    def test_file_not_found(self, mock_rule_ran, mock_stdout):
        mock_rule_ran.return_value = 200
        try:
            sys.argv = ['vsg', '-f', 'no_file.vhd']
            __main__.main()
        except SystemExit as e:
            self.assertEqual(e.code, 1)

        lOutputFile = []
        utils.read_file(sOutputNoFile, lOutputFile)

        lExpected = []
        for sLine in lOutputFile:
            lExpected.append(mock.call(sLine))
            lExpected.append(mock.call('\n'))

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch('sys.stdout')
    @mock.patch('vsg.__main__.rule_list.rule_list.get_number_of_rules_ran')
    def test_file_no_permission(self, mock_rule_ran, mock_stdout):
        pathlib.Path(sNoPermissionFile).touch(mode=0o222, exist_ok=True)
        # exists = pathlib.Path('vsg/tests/source_file/'+sNoPermissionFile).exists()
        # self.assertEqual(exists, "1")

        mock_rule_ran.return_value = 200
        try:
            sys.argv = ['vsg', '-f', sNoPermissionFile]
            __main__.main()
        except SystemExit as e:
            self.assertEqual(e.code, 1)

        lOutputFile = []
        utils.read_file(sOutputNoPermission, lOutputFile)

        lExpected = []
        for sLine in lOutputFile:
            lExpected.append(mock.call(sLine))
            lExpected.append(mock.call('\n'))

        mock_stdout.write.assert_has_calls(lExpected)

    @mock.patch('sys.stdout')
    @mock.patch('vsg.__main__.rule_list.rule_list.get_number_of_rules_ran')
    def test_file_empty(self, mock_rule_ran, mock_stdout):

        mock_rule_ran.return_value = 200
        try:
            sys.argv = ['vsg', '-f', 'vsg/tests/source_file/empty_file.vhd']
            __main__.main()
        except SystemExit as e:
            self.assertEqual(e.code, 1)

        lOutputFile = []
        utils.read_file(sOutputEmptyFile, lOutputFile)

        lExpected = []
        for sLine in lOutputFile:
            lExpected.append(mock.call(sLine))
            lExpected.append(mock.call('\n'))

        mock_stdout.write.assert_has_calls(lExpected)
