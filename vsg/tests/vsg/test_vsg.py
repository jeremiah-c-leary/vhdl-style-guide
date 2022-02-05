import pathlib
import unittest
from unittest import mock
import subprocess
import os

from tempfile import TemporaryFile

from vsg.tests import utils
from vsg import version

class command_line_args():
    ''' This is used as an input into the version command.'''
    def __init__(self, version=False):
        self.version = version


class testVsg(unittest.TestCase):

    def setUp(self):
        if os.path.isfile('deleteme.json'):
            os.remove('deleteme.json')

    def tearDown(self):
        if os.path.isfile('deleteme.json'):
            os.remove('deleteme.json')


    def test_multiple_configuration_w_multiple_filelists(self):
        lExpected = []
        lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.')
        lExpected.append('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.')
        lExpected.append('')

        try:
            subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_1.json','vsg/tests/vsg/config_2.json','--output_format','syntastic'])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus,1)

        self.assertEqual(lActual, lExpected)

    def test_single_configuration_w_filelist(self):
        lExpected = []
        lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.')
        lExpected.append('')

        try:
            subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_1.json','--output_format','syntastic'])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus,1)

        self.assertEqual(lActual, lExpected)

        lExpected = []
        lExpected.append('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.')
        lExpected.append('')

        try:
            subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_2.json','--output_format','syntastic'])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus,1)

        self.assertEqual(lActual, lExpected)

    def test_single_configuration_w_rule_disable(self):
        lExpected = []
        lExpected.append('')

        lActual = subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_3.json','--output_format','syntastic','-f','vsg/tests/vsg/entity1.vhd'])
        lActual = str(lActual.decode('utf-8')).split('\n')
        self.assertEqual(lActual, lExpected)

    def test_multiple_configuration_w_rule_disable(self):
        lExpected = []
        lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.')
        lExpected.append('')

        try:
            subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_3.json','vsg/tests/vsg/config_4.json','--output_format','syntastic','-f','vsg/tests/vsg/entity1.vhd'])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus,1)

        self.assertEqual(lActual, lExpected)

    def test_reverse_multiple_configuration_w_rule_disable(self):
        lExpected = []
        lExpected.append('')

        lActual = subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_4.json','vsg/tests/vsg/config_3.json','--output_format','syntastic','-f','vsg/tests/vsg/entity1.vhd'])
        lActual = str(lActual.decode('utf-8')).split('\n')
        self.assertEqual(lActual, lExpected)

    def test_invalid_configuration(self):
        utils.remove_file('vsg/tests/vsg/config_error.actual.xml')
        lExpected = []
        lExpected.append('ERROR: Invalid configuration file: vsg/tests/vsg/config_error.json')
        lExpected.append('while parsing a flow node')
        lExpected.append('expected the node content, but found \',\'')
        lExpected.append('  in "vsg/tests/vsg/config_error.json", line 2, column 16')
        lExpected.append('')
        try:
            lActual = subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_error.json','--output_format','syntastic','-f','vsg/tests/vsg/entity1.vhd','--junit','vsg/tests/vsg/config_error.actual.xml'])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(lActual, lExpected)
        self.assertEqual(iExitStatus,1)

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

    def test_local_rules(self):
        lExpected = ['ERROR: vsg/tests/vsg/entity_architecture.vhd(1)localized_001 -- Split entity and architecture into seperate files.']
        lExpected.append('')

        try:
            subprocess.check_output(['bin/vsg', '--style', 'jcl', '-f', 'vsg/tests/vsg/entity_architecture.vhd', '-of', 'syntastic', '-lr', 'vsg/tests/vsg/local_rules'])
            iExitStatus = 0
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus,1)

        self.assertEqual(lActual, lExpected)

    def test_invalid_local_rule_directory(self):
        lExpected = ['ERROR: encountered FileNotFoundError, No such file or directory vsg/tests/vsg/invalid_local_rule_directory when trying to open local rules file.', '']

        try:
            lActual = subprocess.check_output(['bin/vsg', '-f', 'vsg/tests/vsg/entity_architecture.vhd', '-of', 'syntastic', '-lr', 'vsg/tests/vsg/invalid_local_rule_directory'])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)
        self.assertEqual(lActual, lExpected)

    def test_globbing_filenames_in_configuration(self):
        lExpected = []
        lExpected.append('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.')
        lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.')
        lExpected.append('')

        try:
            subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_glob.json','--output_format','syntastic'])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

#        print(lActual)
#        print(lExpected)
        self.assertEqual(iExitStatus,1)
        if lActual[0] == lExpected[1]:
            lExpected = []
            lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.')
            lExpected.append('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.')
            lExpected.append('')

        self.assertEqual(lActual, lExpected)

    def test_single_yaml_configuration_w_filelist(self):
        lExpected = []
        lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.')
        lExpected.append('')

        try:
            subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_1.yaml','--output_format','syntastic'])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus,1)

        self.assertEqual(lActual, lExpected)

        lExpected = []
        lExpected.append('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.')
        lExpected.append('')

        try:
            subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_2.json','--output_format','syntastic'])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus,1)

        self.assertEqual(lActual, lExpected)

    def test_multiple_yaml_configuration_w_multiple_filelists(self):
        lExpected = []
        lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.')
        lExpected.append('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.')
        lExpected.append('')

        try:
            subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_1.yaml','vsg/tests/vsg/config_2.yaml','--output_format','syntastic'])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus,1)

        self.assertEqual(lActual, lExpected)

    def test_single_yaml_configuration_w_rule_disable(self):
        lExpected = []
        lExpected.append('')

        lActual = subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_3.yaml','--output_format','syntastic','-f','vsg/tests/vsg/entity1.vhd'])
        lActual = str(lActual.decode('utf-8')).split('\n')
        self.assertEqual(lActual, lExpected)

    def test_multiple_yaml_configuration_w_rule_disable(self):
        lExpected = []
        lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.')
        lExpected.append('')

        try:
            subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_3.yaml','vsg/tests/vsg/config_4.yaml','--output_format','syntastic','-f','vsg/tests/vsg/entity1.vhd'])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus,1)

        self.assertEqual(lActual, lExpected)

    def test_reverse_yaml_multiple_configuration_w_rule_disable(self):
        lExpected = []
        lExpected.append('')

        lActual = subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_4.yaml','vsg/tests/vsg/config_3.yaml','--output_format','syntastic','-f','vsg/tests/vsg/entity1.vhd'])
        lActual = str(lActual.decode('utf-8')).split('\n')
        self.assertEqual(lActual, lExpected)

    def test_globbing_filenames_in_yaml_configuration(self):
        lExpected = []
        lExpected.append('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.')
        lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.')
        lExpected.append('')

        try:
            subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_glob.yaml','--output_format','syntastic'])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus,1)

        if lActual[0] == lExpected[1]:
            lExpected = []
            lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change number of spaces after *in* to 4.')
            lExpected.append('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change number of spaces after *out* to 3.')
            lExpected.append('')

        self.assertEqual(lActual, lExpected)

    def test_oc_command_line_argument(self):
        lExpected = []
        lExpected.append('')

        lActual = subprocess.check_output(['bin/vsg','-oc','deleteme.json'])
        lActual = str(lActual.decode('utf-8')).split('\n')
        self.assertEqual(lActual, lExpected)

    @unittest.skip('Version is performing git commands and is impossible to predict the output.')
    def test_version_command_line_argument(self):
        lExpected = []
        lExpected.append('VHDL Style Guide (VSG) version: ' + str(version.sVersion))

        lActual = subprocess.check_output(['bin/vsg','--version'])
        lActual = str(lActual.decode('utf-8')).split('\n')
        self.assertEqual(lExpected[0], lActual[0])

    def test_missing_configuration_file(self):
        try:
            subprocess.check_output(['bin/vsg', '-c', 'missing_configuration.yaml'])
        except subprocess.CalledProcessError as e:
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)

    @unittest.skipIf('SUDO_UID' in os.environ.keys() or os.geteuid() == 0, "We are root. Root always has permissions so test will fail.")
    def test_no_permission_configuration_file(self):
        sNoPermissionFile = 'no_permission.yml'
        pathlib.Path(sNoPermissionFile).touch(mode=0o222, exist_ok=True)

        sExpected = f'ERROR: encountered PermissionError, Permission denied while opening configuration file: {sNoPermissionFile}\n'

        try:
            subprocess.check_output(['bin/vsg', '-c', sNoPermissionFile])
        except subprocess.CalledProcessError as e:
            sActual = str(e.output.decode('utf-8'))
            iExitStatus = e.returncode

            self.assertEqual(iExitStatus, 1)

            self.assertEqual(sActual, sExpected)
        finally:
            if os.path.isfile(sNoPermissionFile):
                os.remove(sNoPermissionFile)

    def test_missing_files_in_configuration_file(self):
        lExpected = []
        lExpected.append('ERROR: Could not find file missing_file.vhd in configuration file vsg/tests/vsg/missing_file_config.yaml')
        lExpected.append('')

        try:
            subprocess.check_output(['bin/vsg','-c', 'vsg/tests/vsg/missing_file_config.yaml','--output_format','syntastic'])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus,1)

        self.assertEqual(lActual, lExpected)

    def test_summary_output_format_error(self):
        lExpectedStdErr = ['File: vsg/tests/vsg/entity_architecture.vhd ERROR (200 rules checked) [Error: 11] [Warning: 0]', '']
        lExpectedStdOut = ['']

        try:
            subprocess.check_output(['bin/vsg', '-f', 'vsg/tests/vsg/entity_architecture.vhd', '-of', 'summary'], stderr=subprocess.PIPE)
            iExitStatus = 0
        except subprocess.CalledProcessError as e:
            lActualStdOut = str(e.output.decode('utf-8')).split('\n')
            lActualStdErr = str(e.stderr.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)

        self.assertEqual(utils.replace_total_count_summary(lActualStdErr), lExpectedStdErr)
        self.assertEqual(utils.replace_total_count_summary(lActualStdOut), lExpectedStdOut)

    def test_summary_output_format_error_with_local_rules(self):
        lExpectedStdErr = ['File: vsg/tests/vsg/entity_architecture.vhd ERROR (200 rules checked) [Error: 1] [Warning: 0]', '']
        lExpectedStdOut = ['']

        try:
            subprocess.check_output(['bin/vsg', '-f', 'vsg/tests/vsg/entity_architecture.vhd', '-of', 'summary', '-lr', 'vsg/tests/vsg/local_rules'], stderr=subprocess.PIPE)
            iExitStatus = 0
        except subprocess.CalledProcessError as e:
            lActualStdOut = str(e.output.decode('utf-8')).split('\n')
            lActualStdErr = str(e.stderr.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)

        self.assertEqual(utils.replace_total_count_summary(lActualStdErr), lExpectedStdErr)
        self.assertEqual(utils.replace_total_count_summary(lActualStdOut), lExpectedStdOut)

    def test_summary_output_format_ok(self):
        lExpected = ['File: vsg/tests/vsg/entity_architecture.fixed.vhd OK (200 rules checked) [Error: 0] [Warning: 0]', '']

        lActual = subprocess.check_output(
                ['bin/vsg', '-f', 'vsg/tests/vsg/entity_architecture.fixed.vhd', '-of', 'summary'],
                stderr=subprocess.STDOUT
                ).decode('utf-8').split('\n')

        self.assertEqual(utils.replace_total_count_summary(lActual), lExpected)

    def test_summary_output_format_multiple_mixed(self):
        lExpectedStdErr = [
                'File: vsg/tests/vsg/entity_architecture.vhd ERROR (200 rules checked) [Error: 11] [Warning: 0]',
                'File: vsg/tests/vsg/entity1.vhd ERROR (200 rules checked) [Error: 1] [Warning: 0]',
                'File: vsg/tests/vsg/entity2.vhd ERROR (200 rules checked) [Error: 1] [Warning: 0]',
                '',
                ]
        lExpectedStdOut = ['File: vsg/tests/vsg/entity_architecture.fixed.vhd OK (200 rules checked) [Error: 0] [Warning: 0]', '']

        try:
            subprocess.check_output(
                    [
                        'bin/vsg',
                        '-f',
                        'vsg/tests/vsg/entity_architecture.vhd',
                        'vsg/tests/vsg/entity_architecture.fixed.vhd',
                        'vsg/tests/vsg/entity1.vhd',
                        'vsg/tests/vsg/entity2.vhd',
                        '--output_format',
                        'summary'
                    ],
                    stderr=subprocess.PIPE
                    )
            iExitStatus = 0
        except subprocess.CalledProcessError as e:
            lActualStdOut = str(e.output.decode('utf-8')).split('\n')
            lActualStdErr = str(e.stderr.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)

        self.assertEqual(utils.replace_total_count_summary(lActualStdErr), lExpectedStdErr)
        self.assertEqual(utils.replace_total_count_summary(lActualStdOut), lExpectedStdOut)

    def test_summary_output_format_multiple_mixed_jobs_1(self):
        lExpectedStdErr = [
                'File: vsg/tests/vsg/entity_architecture.vhd ERROR (200 rules checked) [Error: 11] [Warning: 0]',
                'File: vsg/tests/vsg/entity1.vhd ERROR (200 rules checked) [Error: 1] [Warning: 0]',
                'File: vsg/tests/vsg/entity2.vhd ERROR (200 rules checked) [Error: 1] [Warning: 0]',
                '',
                ]
        lExpectedStdOut = ['File: vsg/tests/vsg/entity_architecture.fixed.vhd OK (200 rules checked) [Error: 0] [Warning: 0]', '']

        try:
            subprocess.check_output(
                    [
                        'bin/vsg',
                        '-f',
                        'vsg/tests/vsg/entity_architecture.vhd',
                        'vsg/tests/vsg/entity_architecture.fixed.vhd',
                        'vsg/tests/vsg/entity1.vhd',
                        'vsg/tests/vsg/entity2.vhd',
                        '--output_format',
                        'summary',
                        '--jobs=1',
                    ],
                    stderr=subprocess.PIPE
                    )
            iExitStatus = 0
        except subprocess.CalledProcessError as e:
            lActualStdOut = str(e.output.decode('utf-8')).split('\n')
            lActualStdErr = str(e.stderr.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)

        self.assertEqual(utils.replace_total_count_summary(lActualStdErr), lExpectedStdErr)
        self.assertEqual(utils.replace_total_count_summary(lActualStdOut), lExpectedStdOut)


    def test_summary_output_format_multiple_mixed_jobs_2(self):
        lExpectedStdErr = [
                'File: vsg/tests/vsg/entity_architecture.vhd ERROR (200 rules checked) [Error: 11] [Warning: 0]',
                'File: vsg/tests/vsg/entity1.vhd ERROR (200 rules checked) [Error: 1] [Warning: 0]',
                'File: vsg/tests/vsg/entity2.vhd ERROR (200 rules checked) [Error: 1] [Warning: 0]',
                '',
                ]
        lExpectedStdOut = ['File: vsg/tests/vsg/entity_architecture.fixed.vhd OK (200 rules checked) [Error: 0] [Warning: 0]', '']

        try:
            subprocess.check_output(
                    [
                        'bin/vsg',
                        '-f',
                        'vsg/tests/vsg/entity_architecture.vhd',
                        'vsg/tests/vsg/entity_architecture.fixed.vhd',
                        'vsg/tests/vsg/entity1.vhd',
                        'vsg/tests/vsg/entity2.vhd',
                        '--output_format',
                        'summary',
                        '-p 2',
                    ],
                    stderr=subprocess.PIPE
                    )
            iExitStatus = 0
        except subprocess.CalledProcessError as e:
            lActualStdOut = str(e.output.decode('utf-8')).split('\n')
            lActualStdErr = str(e.stderr.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus, 1)

        self.assertEqual(utils.replace_total_count_summary(lActualStdErr), lExpectedStdErr)
        self.assertEqual(utils.replace_total_count_summary(lActualStdOut), lExpectedStdOut)


    @unittest.skip('Version is performing git commands and is impossible to predict the output.')
    @mock.patch('sys.stdout')
    def test_version(self, mockStdout):
        oCommandLineArguments = command_line_args(True)
        try:
            version.print_version(oCommandLineArguments)
        except SystemExit:
            pass

        mockStdout.write.assert_has_calls([
            mock.call('VHDL Style Guide (VSG) version: ' + str(version.sVersion)),
            mock.call('\n')
        ])
