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
        lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change the number of spaces after the "in" keyword to four spaces.')
        lExpected.append('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change the number of spaces after the "out" keyword to three spaces.')
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
        lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change the number of spaces after the "in" keyword to four spaces.')
        lExpected.append('')

        try:
            subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_1.json','--output_format','syntastic'])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus,1)

        self.assertEqual(lActual, lExpected)

        lExpected = []
        lExpected.append('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change the number of spaces after the "out" keyword to three spaces.')
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
        lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change the number of spaces after the "in" keyword to four spaces.')
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

    @mock.patch('sys.stderr')
    def test_invalid_configuration(self, mockStderr):
        utils.remove_file('vsg/tests/vsg/config_error.actual.xml')
        lExpected = []
        lExpected.append('ERROR: Invalid configuration file: vsg/tests/vsg/config_error.json')
        lExpected.append('while parsing a flow node')
        lExpected.append('expected the node content, but found \',\'')
        lExpected.append('  in "vsg/tests/vsg/config_error.json", line 2, column 16')
        lExpected.append('')

        try:
            lActual = subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_error.json','--output_format','syntastic','-f','vsg/tests/vsg/entity1.vhd','--junit','vsg/tests/vsg/config_error.actual.xml'], stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(lActual, lExpected)
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

        self.assertEqual(iExitStatus,1)

        # Clean up
        utils.remove_file('vsg/tests/vsg/config_error.actual.xml')

    def test_local_rules(self):
        lExpected = ['ERROR: vsg/tests/vsg/entity_architecture.vhd(1)localized_001 -- Split entity and architecture into seperate files.']
        lExpected.append('')

        try:
            subprocess.check_output(['bin/vsg', '-f', 'vsg/tests/vsg/entity_architecture.vhd', '-of', 'syntastic', '-lr', 'vsg/tests/vsg/local_rules'])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus,1)

        self.assertEqual(lActual, lExpected)

    def test_invalid_local_rule_directory(self):
        lExpected = ['ERROR: specified local rules directory vsg/tests/vsg/invalid_local_rule_directory could not be found.']
        lExpected.append('')
        lActual = subprocess.check_output(['bin/vsg', '-f', 'vsg/tests/vsg/entity_architecture.vhd', '-of', 'syntastic', '-lr', 'vsg/tests/vsg/invalid_local_rule_directory'])
        lActual = str(lActual.decode('utf-8')).split('\n')
        self.assertEqual(lActual, lExpected)

    def test_globbing_filenames_in_configuration(self):
        lExpected = []
        lExpected.append('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change the number of spaces after the "out" keyword to three spaces.')
        lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change the number of spaces after the "in" keyword to four spaces.')
        lExpected.append('')

        try:
            subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_glob.json','--output_format','syntastic'])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus,1)
        if lActual[0] == lExpected[1]:
            lExpected = []
            lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change the number of spaces after the "in" keyword to four spaces.')
            lExpected.append('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change the number of spaces after the "out" keyword to three spaces.')
            lExpected.append('')

        self.assertEqual(lActual, lExpected)

    def test_single_yaml_configuration_w_filelist(self):
        lExpected = []
        lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change the number of spaces after the "in" keyword to four spaces.')
        lExpected.append('')

        try:
            subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_1.yaml','--output_format','syntastic'])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus,1)

        self.assertEqual(lActual, lExpected)

        lExpected = []
        lExpected.append('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change the number of spaces after the "out" keyword to three spaces.')
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
        lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change the number of spaces after the "in" keyword to four spaces.')
        lExpected.append('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change the number of spaces after the "out" keyword to three spaces.')
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
        lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change the number of spaces after the "in" keyword to four spaces.')
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
        lExpected.append('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change the number of spaces after the "out" keyword to three spaces.')
        lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change the number of spaces after the "in" keyword to four spaces.')
        lExpected.append('')

        try:
            subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_glob.yaml','--output_format','syntastic'])
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus,1)

        if lActual[0] == lExpected[1]:
            lExpected = []
            lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change the number of spaces after the "in" keyword to four spaces.')
            lExpected.append('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change the number of spaces after the "out" keyword to three spaces.')
            lExpected.append('')

        self.assertEqual(lActual, lExpected)

    def test_oc_command_line_argument(self):
        lExpected = []
        lExpected.append('')

        lActual = subprocess.check_output(['bin/vsg','-oc','deleteme.json'])
        lActual = str(lActual.decode('utf-8')).split('\n')
        self.assertEqual(lActual, lExpected)

    def test_version_command_line_argument(self):
        lExpected = []
        lExpected.append('VHDL Style Guide (VSG) version ' + version.version)

        lActual = subprocess.check_output(['bin/vsg','--version'])
        lActual = str(lActual.decode('utf-8')).split('\n')
        self.assertEqual(lExpected[0], lActual[0])

    @mock.patch('sys.stderr')
    def test_missing_configuration_file(self, mockStderr):
        lExpected = []
        lExpected.append('ERROR: Could not find configuration file: missing_configuration.yaml')
        lExpected.append('')

        try:
            subprocess.check_output(['bin/vsg','-c', 'missing_configuration.yaml'], stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            lActual = str(e.output.decode('utf-8')).split('\n')
            iExitStatus = e.returncode

        self.assertEqual(iExitStatus,1)

        self.assertEqual(lActual, lExpected)

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



    @mock.patch('sys.stdout')
    def test_version(self, mockStdout):
        oCommandLineArguments = command_line_args(True)
        try:
            version.print_version(oCommandLineArguments)
        except SystemExit:
            pass

        mockStdout.write.assert_has_calls([
            mock.call('VHDL Style Guide (VSG) version ' + version.version),
            mock.call('\n')
        ])
