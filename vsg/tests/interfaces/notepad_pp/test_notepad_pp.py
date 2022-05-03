
import vsg

import vsg.interfaces.notepad_pp

import os

import unittest

from vsg.tests import utils

lFile = []
utils.read_file(os.path.join(os.path.dirname(__file__),'test_input.vhd'), lFile)
sFile = '\n'.join(lFile)

lFileFixedStyleJcl = []
utils.read_file(os.path.join(os.path.dirname(__file__),'test_input.fixed_jcl_style.vhd'), lFileFixedStyleJcl)

lFileFixedConfig1 = []
utils.read_file(os.path.join(os.path.dirname(__file__),'test_input.fixed_config_1.vhd'), lFileFixedConfig1)

lFileFixedConfig2 = []
utils.read_file(os.path.join(os.path.dirname(__file__),'test_input.fixed_config_2.vhd'), lFileFixedConfig2)

lExpectedOutput = []
lExpectedOutput.append('================================================================================')
lExpectedOutput.append('File:  None')
lExpectedOutput.append('================================================================================')
lExpectedOutput.append('Phase 7 of 7... Reporting')
lExpectedOutput.append('Total Rules Checked: 627')
lExpectedOutput.append('Total Violations:    0')
lExpectedOutput.append('  Error   :     0')
lExpectedOutput.append('  Warning :     0')

sExpectedOutput = '\n'.join(lExpectedOutput)
sExpectedOutput += '\n'


class test_interface(unittest.TestCase):

    def setUp(self):
        self.oInterface = vsg.interfaces.notepad_pp.New()

    def test_interface_exists(self):
        self.assertEqual('notepad++ interface', self.oInterface.identifier)

    def test_interface_fix_method(self):
        oInputArguments = self.oInterface.get_input_arguments()
        oInputArguments.set_text('LIBRARY ieee;')
        oResults = self.oInterface.fix(oInputArguments)
        sUpdatedText = oResults.get_text()
        self.assertEqual('library ieee;', sUpdatedText)

    def test_interface_fix_method_with_jcl_style(self):
        oInputArguments = self.oInterface.get_input_arguments()
        oInputArguments.set_text(sFile)
        oInputArguments.set_style('jcl')
        oResults = self.oInterface.fix(oInputArguments)
        sUpdatedText = oResults.get_text()
        self.assertEqual(lFileFixedStyleJcl, sUpdatedText.splitlines())
        sOutput = oResults.get_stdout()
        self.assertEqual(sExpectedOutput, sOutput)
        self.assertFalse(oResults.has_violations())

    def test_interface_fix_method_with_jcl_style_with_violations(self):
        oInputArguments = self.oInterface.get_input_arguments()
        oInputArguments.set_text(sFile)
        oInputArguments.set_style('jcl')
        oInputArguments.add_configuration(os.path.join(os.path.dirname(__file__), 'config_violation.yaml'))
        oResults = self.oInterface.fix(oInputArguments)
        self.assertTrue(oResults.has_violations())

    def test_interface_fix_method_with_one_configuration(self):
        oInputArguments = self.oInterface.get_input_arguments()
        oInputArguments.set_text(sFile)
        oInputArguments.add_configuration(os.path.join(os.path.dirname(__file__), 'config_1.yaml'))
        oResults = self.oInterface.fix(oInputArguments)
        sUpdatedText = oResults.get_text()
        self.assertEqual(lFileFixedConfig1, sUpdatedText.splitlines())

    def test_interface_fix_method_with_two_configurations(self):
        oInputArguments = self.oInterface.get_input_arguments()
        oInputArguments.set_text(sFile)
        oInputArguments.add_configuration(os.path.join(os.path.dirname(__file__), 'config_1.yaml'))
        oInputArguments.add_configuration(os.path.join(os.path.dirname(__file__), 'config_2.yaml'))
        oResults = self.oInterface.fix(oInputArguments)
        sUpdatedText = oResults.get_text()
        self.assertEqual(lFileFixedConfig2, sUpdatedText.splitlines())


class test_input_arguments(unittest.TestCase):

    def setUp(self):
        self.oInterface = vsg.interfaces.notepad_pp.New()
        self.oInputArguments = self.oInterface.get_input_arguments()

    def test_get_input_arguments_set_text_method(self):
        self.assertIsNone(self.oInputArguments.text)
        self.oInputArguments.set_text('This is a test.')
        self.assertEqual('This is a test.', self.oInputArguments.text)
        
