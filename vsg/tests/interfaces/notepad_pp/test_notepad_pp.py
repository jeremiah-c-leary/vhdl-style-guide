
import vsg

import vsg.interfaces.notepad_pp

import os

import re

import unittest

from vsg.tests import utils

lFile = []
utils.read_file(os.path.join(os.path.dirname(__file__),'test_input.vhd'), lFile)
sFile = '\n'.join(lFile)

lFileSyntaxError = []
utils.read_file(os.path.join(os.path.dirname(__file__),'test_input.syntax_error.vhd'), lFileSyntaxError)
sFileSyntaxError = '\n'.join(lFileSyntaxError)

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
lExpectedOutput.append('Total Rules Checked: replaced')
lExpectedOutput.append('Total Violations:    0')
lExpectedOutput.append('  Error   :     0')
lExpectedOutput.append('  Warning :     0')

sExpectedOutput = '\n'.join(lExpectedOutput)
sExpectedOutput += '\n'

sExpectedSyntaxErrorOutput = ''
sExpectedSyntaxErrorOutput += '\n'
sExpectedSyntaxErrorOutput += 'Error: Unexpected token detected while parsing architecture_body @ Line 6, Column 1 in file None\n'
sExpectedSyntaxErrorOutput += '       Expecting : begin\n'
sExpectedSyntaxErrorOutput += '       Found     : end\n'

sExpectedConfigurationErrorOutput = ''
sExpectedConfigurationErrorOutput += 'ERROR: Invalid configuration of file None\n'
sExpectedConfigurationErrorOutput += 'ERROR [config-001] Rule architecture_002 has been deprecated.\n'
sExpectedConfigurationErrorOutput += '  Rule architecture_002 has been split into the following rules:\n'
sExpectedConfigurationErrorOutput += '    architecture_030\n'
sExpectedConfigurationErrorOutput += '    architecture_031\n'
sExpectedConfigurationErrorOutput += '    architecture_032\n'
sExpectedConfigurationErrorOutput += '    architecture_033\n'


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
        sOutput = re.sub(r'Total Rules Checked: [0-9][0-9]*', r'Total Rules Checked: replaced', sOutput)
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

    def test_interface_fix_method_with_syntax_error(self):
        oInputArguments = self.oInterface.get_input_arguments()
        oInputArguments.set_text(sFileSyntaxError)

        oResults = self.oInterface.fix(oInputArguments)

        self.assertTrue(oResults.error_status())
        self.assertFalse(oResults.has_violations())

        sUpdatedText = oResults.get_text()
        self.assertEqual(lFileSyntaxError, sUpdatedText.splitlines())

        sOutput = oResults.get_stdout()
        self.assertEqual(sExpectedSyntaxErrorOutput, sOutput)

    def test_interface_fix_method_with_configuration_error(self):
        oInputArguments = self.oInterface.get_input_arguments()
        oInputArguments.set_text(sFile)
        oInputArguments.add_configuration(os.path.join(os.path.dirname(__file__), 'config_error.yaml'))

        oResults = self.oInterface.fix(oInputArguments)

        self.assertTrue(oResults.error_status())
        self.assertFalse(oResults.has_violations())

        sUpdatedText = oResults.get_text()
        self.assertEqual(lFile, sUpdatedText.splitlines())

        sOutput = oResults.get_stdout()
        self.assertEqual(sExpectedConfigurationErrorOutput, sOutput)



class test_input_arguments(unittest.TestCase):

    def setUp(self):
        self.oInterface = vsg.interfaces.notepad_pp.New()
        self.oInputArguments = self.oInterface.get_input_arguments()

    def test_get_input_arguments_set_text_method(self):
        self.assertIsNone(self.oInputArguments.text)
        self.oInputArguments.set_text('This is a test.')
        self.assertEqual('This is a test.', self.oInputArguments.text)
        
