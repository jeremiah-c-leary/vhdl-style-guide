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
        lExpected = ['vsg', '--filename', 'filename', '--output_format', 'vsg', '--local_rules', '$COMPANY_LOCAL_RULES_DIR', '--configuration', 'vsg/tests/program_config/config_dir/config1.yaml', 'vsg/tests/program_config/config_dir/config2.yaml', '--fix', '--fix_phase', '7', '--junit', 'vsg_results.xml']

        dProgramFile = program_config.read_home_program_file()

        program_config.update_sys_args()

        self.assertEqual(len(lExpected), len(sys.argv))
        for iIndex, sEntry in enumerate(lExpected):
            self.assertEqual(sEntry, sys.argv[iIndex])

    @mock.patch('vsg.program_config.sHomeDefaultFile', 'vsg/tests/program_config/configuration_w_globbing.yaml')
    @mock.patch.dict(os.environ,{'TEST_DIR':'vsg/tests/program_config/test_dir', 'CONFIG_DIR':'vsg/tests/program_config/config_dir','COMPANY_LOCAL_RULES_DIR':'vsg/tests/program_config/local_rules'})
    def test_globbing_and_expansion_of_env_variables(self):
        sys.argv = ['vsg', '--output_format', 'vsg']
        lExpected = ['vsg', '--output_format', 'vsg', '--filename', 'vsg/tests/program_config/test_dir/a.vhd', 'vsg/tests/program_config/test_dir/b.vhd', 'vsg/tests/program_config/test_dir/c.vhd', '--local_rules', 'vsg/tests/program_config/local_rules', '--configuration', 'vsg/tests/program_config/config_dir/config1.yaml', 'vsg/tests/program_config/config_dir/config2.yaml', '--fix', '--fix_phase', '7', '--junit', 'vsg_results.xml']

        dProgramFile = program_config.read_home_program_file()

        program_config.update_sys_args()

#        self.assertEqual(len(lExpected), len(sys.argv))
        for iIndex, sEntry in enumerate(lExpected):
            self.assertEqual(sEntry, sys.argv[iIndex])


    @mock.patch.dict(os.environ,{'TEST_DIR':'test_dir_expanded', 'CONFIG_DIR':'config_dir_expanded','COMPANY_LOCAL_RULES_DIR':'company_local_dir_expanded'})
    def test_expand_environment_vars(self):
        dSysArgs = {}
        dSysArgs['command_line_arguments'] = {}
        dSysArgs['command_line_arguments']['fix'] = True

        dExpected = {}
        dExpected['command_line_arguments'] = {}
        dExpected['command_line_arguments']['fix'] = True

        self.assertEqual(program_config.expand_environment_vars(dSysArgs), dExpected)

        dSysArgs['command_line_arguments']['filename'] = []
        dSysArgs['command_line_arguments']['filename'].append('$TEST_DIR/*.vhd')
        dSysArgs['command_line_arguments']['filename'].append('$CONFIG_DIR/my.vhd')
        dSysArgs['command_line_arguments']['filename'].append('$COMPANY_LOCAL_RULES_DIR/other.vhd')

        dExpected['command_line_arguments']['filename'] = []
        dExpected['command_line_arguments']['filename'].append('test_dir_expanded/*.vhd')
        dExpected['command_line_arguments']['filename'].append('config_dir_expanded/my.vhd')
        dExpected['command_line_arguments']['filename'].append('company_local_dir_expanded/other.vhd')

        self.assertEqual(program_config.expand_environment_vars(dSysArgs), dExpected)

        
        dSysArgs['command_line_arguments']['configuration'] = []
        dSysArgs['command_line_arguments']['configuration'].append('$TEST_DIR/*.yaml')
        dSysArgs['command_line_arguments']['configuration'].append('$CONFIG_DIR/*.json')

        dExpected['command_line_arguments']['configuration'] = []
        dExpected['command_line_arguments']['configuration'].append('test_dir_expanded/*.yaml')
        dExpected['command_line_arguments']['configuration'].append('config_dir_expanded/*.json')
        
        self.assertEqual(program_config.expand_environment_vars(dSysArgs), dExpected)

        dSysArgs['command_line_arguments']['junit'] = '$TEST_DIR/junit.xml'

        dExpected['command_line_arguments']['junit'] = 'test_dir_expanded/junit.xml'


        self.assertEqual(program_config.expand_environment_vars(dSysArgs), dExpected)


        dSysArgs['command_line_arguments']['local_rules'] = '$TEST_DIR/local_rules_dir'

        dExpected['command_line_arguments']['local_rules'] = 'test_dir_expanded/local_rules_dir'


        self.assertEqual(program_config.expand_environment_vars(dSysArgs), dExpected)

    def test_glob_files(self):
        dSysArgs = {}
        dSysArgs['command_line_arguments'] = {}
        dSysArgs['command_line_arguments']['fix'] = True

        dExpected = {}
        dExpected['command_line_arguments'] = {}
        dExpected['command_line_arguments']['fix'] = True

        self.assertEqual(program_config.glob_files(dSysArgs), dExpected)

        dSysArgs['command_line_arguments']['filename'] = []
        dSysArgs['command_line_arguments']['filename'].append('vsg/tests/program_config/test_dir/*.vhd')

        dExpected['command_line_arguments']['filename'] = []
        dExpected['command_line_arguments']['filename'].append('vsg/tests/program_config/test_dir/a.vhd')
        dExpected['command_line_arguments']['filename'].append('vsg/tests/program_config/test_dir/b.vhd')
        dExpected['command_line_arguments']['filename'].append('vsg/tests/program_config/test_dir/c.vhd')

        self.assertEqual(program_config.glob_files(dSysArgs), dExpected)

        
        dSysArgs['command_line_arguments']['configuration'] = []
        dSysArgs['command_line_arguments']['configuration'].append('vsg/tests/program_config/config_dir/*.yaml')

        dExpected['command_line_arguments']['configuration'] = []
        dExpected['command_line_arguments']['configuration'].append('vsg/tests/program_config/config_dir/config1.yaml')
        dExpected['command_line_arguments']['configuration'].append('vsg/tests/program_config/config_dir/config2.yaml')
        
        self.assertEqual(program_config.glob_files(dSysArgs), dExpected)

