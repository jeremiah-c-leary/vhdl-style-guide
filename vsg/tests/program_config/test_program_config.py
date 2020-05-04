import sys
import unittest
from unittest import mock
import os

from vsg.tests import utils

from vsg import program_config

class testProgramConfigModule(unittest.TestCase):


    @mock.patch('vsg.program_config.sHomeDefaultFile', 'vsg/tests/program_config/home_default_config.yaml')
    def test_read_home_program_file(self):


        dExpected = {}
        dExpected['command_line_arguments'] = {}
        dExpected['command_line_arguments']['output_format'] = 'syntastic'
        dExpected['command_line_arguments']['junit'] = 'vsg_results.xml'

        dActual = program_config.read_home_program_file()

        self.assertEqual(dExpected, dActual)

    @mock.patch('vsg.program_config.sHomeDefaultFile', 'vsg/tests/program_config/home_default_config.yam')
    def test_read_home_program_file_w_no_home_config_file_preset(self):

        dExpected = {}

        dActual = program_config.read_home_program_file()

        self.assertEqual(dExpected, dActual)


    @mock.patch.dict(os.environ,{'VSG_DEFAULT_CONFIG':'vsg/tests/program_config/env_var_default_config.yaml'})
    def test_read_environment_variable_program_file(self):
        dExpected = {}
      
        dExpected['command_line_arguments'] = {}
        dExpected['command_line_arguments']['output_format'] = 'vsg'
        dExpected['command_line_arguments']['junit'] = 'some_other_vsg_results.xml'

        dActual = program_config.read_environment_variable_program_file({})

        self.assertEqual(dExpected, dActual)

    @mock.patch.dict(os.environ,{'VSG_DEFAULT_CONFIG':'vsg/tests/program_config/env_var_default_config.yam'})
    @mock.patch('sys.stdout')
    def test_read_environment_variable_program_file_w_invalid_environment_variable(self, mockStdout):
        dExpected = {}
      
        dExpected['command_line_arguments'] = {}
        dExpected['command_line_arguments']['output_format'] = 'vsg'
        dExpected['command_line_arguments']['junit'] = 'some_other_vsg_results.xml'

        with self.assertRaises(SystemExit) as cm:
            dActual = program_config.read_environment_variable_program_file({})

        self.assertEqual(cm.exception.code, 1)

        mockStdout.write.assert_has_calls([
            mock.call('ERROR: Could not find configuration file: vsg/tests/program_config/env_var_default_config.yam'),
            mock.call('\n')
        ])

    def test_read_environment_variable_program_file_w_undefined_variable(self):
        dExpected = {}
        dExpected['command_line_arguments'] = {}
        dExpected['command_line_arguments']['output_format'] = 'syntastic'
        dExpected['command_line_arguments']['junit'] = 'vsg_results.xml'
      
        dActual = program_config.read_environment_variable_program_file(dExpected)

        self.assertEqual(dExpected, dActual)

    def test_merge_program_config_w_user_sys_args_w_no_program_config(self):
        sys.argv = ['vsg', '-f', 'filename']
        lExpected = []

        dExpected = {}

        lActual = program_config.merge_program_config_w_user_sys_args(dExpected)

        self.assertEqual(sys.argv, lActual)

    @mock.patch('vsg.program_config.sHomeDefaultFile', 'vsg/tests/program_config/home_default_config.yaml')
    def test_merge_program_config_w_user_sys_args_w_program_config(self):
        sys.argv = ['vsg', '-f', 'filename']
        lExpected = ['vsg', '-f', 'filename', '--output_format', 'syntastic', '--junit', 'vsg_results.xml']

        dProgramFile = program_config.read_home_program_file()

        lActual = program_config.merge_program_config_w_user_sys_args(dProgramFile)

        self.assertEqual(lExpected, lActual)

    @mock.patch('vsg.program_config.sHomeDefaultFile', 'vsg/tests/program_config/home_default_config.yaml')
    def test_merge_program_config_w_user_sys_args_w_program_config_replacing_single_element_argument(self):
        sys.argv = ['vsg', '-f', 'filename', '--output_format', 'vsg']
        lExpected = ['vsg', '-f', 'filename', '--output_format', 'vsg', '--junit', 'vsg_results.xml']

        dProgramFile = program_config.read_home_program_file()

        lActual = program_config.merge_program_config_w_user_sys_args(dProgramFile)

        self.assertEqual(len(lExpected), len(lActual))
        for iIndex, sEntry in enumerate(lExpected):
            self.assertEqual(sEntry, lActual[iIndex])

    @mock.patch('vsg.program_config.sHomeDefaultFile', 'vsg/tests/program_config/configuration_w_lists.yaml')
    def test_update_sys_args_w_user_sys_args_w_full_up_program_config(self):
        sys.argv = ['vsg', '-f', 'filename', '--output_format', 'vsg']
        lExpected = ['vsg', '--filename', 'filename', '--output_format', 'vsg', '--local_rules', '$COMPANY_LOCAL_RULES_DIR', '--configuration', 'config_1.yaml', 'config_2.yaml', '--fix', '--fix_phase', '7', '--junit', 'vsg_results.xml']

        dProgramFile = program_config.read_home_program_file()

        program_config.update_sys_args()

        self.assertEqual(len(lExpected), len(sys.argv))
        for iIndex, sEntry in enumerate(lExpected):
            self.assertEqual(sEntry, sys.argv[iIndex])
