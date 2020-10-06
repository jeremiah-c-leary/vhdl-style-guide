import os

import unittest

from vsg.rules import generic
from vsg import vhdlFile
from vsg.tests import utils


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'generic_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleGenericMethods(unittest.TestCase):

    def test_rule_017(self):
        oRule = generic.rule_017()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '017')

        dExpected = [{'lines':[{'number': 52}], 'words_to_fix': {'STD_LOGIC'}},
                     {'lines':[{'number': 96}], 'words_to_fix': {'STD_LOGIC'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
