
import vsg

import vsg.interfaces.notepad_pp

#import os

import unittest

#from vsg.tests import utils
#import vsg.vhdlFile as vhdlFile
#
#sLrmUnit = utils.extract_lrm_unit_name(__name__)
#
#lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),sLrmUnit,'classification_test_input.vhd'))
#oFile = vhdlFile.vhdlFile(lFile)


class test_interface(unittest.TestCase):

    def setUp(self):
        self.oInterface = vsg.interfaces.notepad_pp.New()

    def test_interface_exists(self):
        self.assertEqual('notepad++ interface', self.oInterface.identifier)

    def test_interface_set_input_arguments(self):
        self.assertIsNone(self.oInterface.inputArguments)
        oInputArguments = self.oInterface.get_input_arguments()
        oInputArguments.set_text('Hello')
        self.oInterface.set_input_arguments(oInputArguments)
        self.assertEqual('Hello', self.oInterface.inputArguments.text)

    def test_interface_execute_method_without_fix(self):
        oInputArguments = self.oInterface.get_input_arguments()
        oInputArguments.set_text('LIBRARY ieee;')
        self.oInterface.set_input_arguments(oInputArguments)
        self.oInterface.execute()
        oResults = self.oInterface.get_results()  
        sUpdatedText = oResults.get_text()
        self.assertEqual('LIBRARY ieee;', sUpdatedText)

    def test_interface_execute_method_with_fix(self):
        oInputArguments = self.oInterface.get_input_arguments()
        oInputArguments.set_text('LIBRARY ieee;')
        oInputArguments.enable_fix()
        self.oInterface.set_input_arguments(oInputArguments)
        self.oInterface.execute()
        oResults = self.oInterface.get_results()  
        sUpdatedText = oResults.get_text()
        self.assertEqual('library ieee;', sUpdatedText)

class test_input_arguments(unittest.TestCase):

    def setUp(self):
        self.oInterface = vsg.interfaces.notepad_pp.New()
        self.oInputArguments = self.oInterface.get_input_arguments()

    def test_get_input_arguments_set_text_method(self):
        self.assertIsNone(self.oInputArguments.text)
        self.oInputArguments.set_text('This is a test.')
        self.assertEqual('This is a test.', self.oInputArguments.text)
        
    def test_get_input_arguments_enable_fix_method(self):
        self.assertFalse(self.oInputArguments.fix_enabled)
        self.oInputArguments.enable_fix()
        self.assertTrue(self.oInputArguments.fix_enabled)

    def test_get_input_arguments_disable_fix_method(self):
        self.assertFalse(self.oInputArguments.fix_enabled)
        self.oInputArguments.enable_fix()
        self.assertTrue(self.oInputArguments.fix_enabled)
        self.oInputArguments.disable_fix()
        self.assertFalse(self.oInputArguments.fix_enabled)

