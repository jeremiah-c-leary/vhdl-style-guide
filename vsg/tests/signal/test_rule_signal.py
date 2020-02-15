import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import signal
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'signal_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleSignalMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = signal.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '001')
        lExpected = [6,8,15]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_002(self):
        oRule = signal.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '002')
        lExpected = [{'line_number': 7, 'words_to_fix': {'Signal'}},
                     {'line_number': 11, 'words_to_fix': {'siGNal'}},
                     {'line_number': 13, 'words_to_fix': {'signAL'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_003(self):
        oRule = signal.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '003')
        lExpected = utils.add_violation_list([8,9,12])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_003_w_3_spaces(self):
        oRule = signal.rule_003()
        oRule.spaces = 3
        lExpected = []
        lExpected.extend(utils.add_violation_list(range(5, 12)))
        lExpected.extend(utils.add_violation_list(range(13, 17)))
        lExpected.extend(utils.add_violation_list(range(18, 22)))
        lExpected.append(utils.add_violation(23))

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_004(self):
        oRule = signal.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '004')
        lExpected = [{'line_number': 6, 'words_to_fix': {'a_SIg'}},
                     {'line_number': 9, 'words_to_fix': {'siG'}},
                     {'line_number': 12, 'words_to_fix': {'SIg'}},
                     {'line_number': 15, 'words_to_fix': {'sIg'}},
                     {'line_number': 20, 'words_to_fix': {'b_Sig2', 'b_siG100'}},
                     {'line_number': 21, 'words_to_fix': {'a_sIg2'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_005(self):
        oRule = signal.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '005')
        lExpected = [6,10,13,14,16,20,21]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_006(self):
        oRule = signal.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '006')
        lExpected = [7,11,19,21]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_007(self):
        oRule = signal.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '007')
        lExpected = [11,16]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_008(self):
        oRule = signal.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '008')
        self.assertTrue(oRule.disable)
        lExpected = [9,12,13,14,15,16,19,21,23]
        oRule.prefixes = ['a_','b_','d_','e_']
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_013(self):
        oRule = signal.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '013')
        lExpected = ['3-25']
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_010(self):
        oRule = signal.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '010')
        lExpected = [{'line_number': 12, 'words_to_fix': {'STD_LOGIC_VECTOR'}},
                     {'line_number': 16, 'words_to_fix': {'STD_LOGIC_VECTOR'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_011(self):
        oRule = signal.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '011')
        lExpected = [{'line_number': 12, 'words_to_fix': {'STD_LOGIC_VECTOR'}},
                     {'line_number': 16, 'words_to_fix': {'STD_LOGIC_VECTOR'}},
                     {'line_number': 23, 'words_to_fix': {'t_User_Defined_Type'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)


