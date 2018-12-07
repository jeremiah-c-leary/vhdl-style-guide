import unittest
import subprocess
import os

from vsg.tests import utils


class testVsg(unittest.TestCase):

    def test_multiple_configuration_w_multiple_filelists(self):
        lExpected = []
        lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change the number of spaces after the "in" keyword to four spaces.')
        lExpected.append('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change the number of spaces after the "out" keyword to three spaces.')
        lExpected.append('')

        lActual = subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_1.json','vsg/tests/vsg/config_2.json','--output_format','syntastic']).split('\n')
        self.assertEqual(lActual, lExpected)

    def test_single_configuration_w_filelist(self):
        lExpected = []
        lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change the number of spaces after the "in" keyword to four spaces.')
        lExpected.append('')

        lActual = subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_1.json','--output_format','syntastic']).split('\n')
        self.assertEqual(lActual, lExpected)

        lExpected = []
        lExpected.append('ERROR: vsg/tests/vsg/entity2.vhd(8)port_008 -- Change the number of spaces after the "out" keyword to three spaces.')
        lExpected.append('')

        lActual = subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_2.json','--output_format','syntastic']).split('\n')
        self.assertEqual(lActual, lExpected)

    def test_single_configuration_w_rule_disable(self):
        lExpected = []
        lExpected.append('')

        lActual = subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_3.json','--output_format','syntastic','-f','vsg/tests/vsg/entity1.vhd']).split('\n')
        self.assertEqual(lActual, lExpected)

    def test_multiple_configuration_w_rule_disable(self):
        lExpected = []
        lExpected.append('ERROR: vsg/tests/vsg/entity1.vhd(7)port_007 -- Change the number of spaces after the "in" keyword to four spaces.')
        lExpected.append('')

        lActual = subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_3.json','vsg/tests/vsg/config_4.json','--output_format','syntastic','-f','vsg/tests/vsg/entity1.vhd']).split('\n')
        self.assertEqual(lActual, lExpected)

    def test_reverse_multiple_configuration_w_rule_disable(self):
        lExpected = []
        lExpected.append('')

        lActual = subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_4.json','vsg/tests/vsg/config_3.json','--output_format','syntastic','-f','vsg/tests/vsg/entity1.vhd']).split('\n')
        self.assertEqual(lActual, lExpected)

    def test_invalid_configuration(self):
        utils.remove_file('vsg/tests/vsg/config_error.actual.xml')
        lExpected = []
        lExpected.append('Error in JSON file: vsg/tests/vsg/config_error.json')
        lExpected.append('')

        lActual = subprocess.check_output(['bin/vsg','--configuration','vsg/tests/vsg/config_error.json','--output_format','syntastic','-f','vsg/tests/vsg/entity1.vhd','--junit','vsg/tests/vsg/config_error.actual.xml']).split('\n')
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
                self.assertEqual(lExpected[iLineNumber], lActual[iLineNumber])
        # Clean up
        utils.remove_file('vsg/tests/vsg/config_error.actual.xml')
