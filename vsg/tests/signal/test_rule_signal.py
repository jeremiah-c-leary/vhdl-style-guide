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
        lExpected = [7,11,13]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_003(self):
        oRule = signal.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '003')
        lExpected = [8,9,12]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_003_w_3_spaces(self):
        oRule = signal.rule_003()
        oRule.spaces = 3
        lExpected = []
        lExpected.extend(range(5, 12))
        lExpected.extend(range(13, 17))
        lExpected.extend(range(18, 22))
        lExpected.append(23)
  
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_004(self):
        oRule = signal.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '004')
        lExpected = [6,9,12,15,20,21]
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

    def test_rule_008_with_no_prefixes(self):
        oRule = signal.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '008')
        lExpected = []
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_008_with_prefixes(self):
        oRule = signal.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '008')
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
        lExpected = [12,16]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_011(self):
        oRule = signal.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '011')
        lExpected = [12,16,23]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)


