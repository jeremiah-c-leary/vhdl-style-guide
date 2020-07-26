import os

import unittest

from vsg.rules import library
from vsg import vhdlFile
from vsg.tests import utils


# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','library','library_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleLibraryMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = library.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '001')

        lExpected = []

        dViolation = utils.add_violation(7)
        dViolation['action'] = 'remove'
        dViolation['solution'] = 'Remove spaces before "library"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(9)
        dViolation['action'] = 'remove'
        dViolation['solution'] = 'Remove spaces before "Library"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(21)
        dViolation['action'] = 'remove'
        dViolation['solution'] = 'Remove spaces before "library"'
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(lExpected, oRule.violations)

    def test_rule_002(self):
        oRule = library.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '002')

        lExpected = []

        dViolation = utils.add_violation(13)
        dViolation['solution'] = 'Ensure there are only 1 space(s) between "library" and "lib4"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(20)
        dViolation['solution'] = 'Ensure there are only 1 space(s) between "LIBRARY" and "lib5"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(21)
        dViolation['solution'] = 'Ensure there are only 1 space(s) between "library" and "lib6"'
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(lExpected, oRule.violations)

    def test_rule_003(self):
        oRule = library.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '003')

        lExpected = [utils.add_violation(21)]
        oRule.analyze(oFile)
        self.assertEqual(lExpected, oRule.violations)

    def test_rule_004(self):
        oRule = library.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '004')

        lExpected = []
        dViolation = utils.add_violation(9)
        dViolation['solution'] = 'Change "Library" to "library"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(20)
        dViolation['solution'] = 'Change "LIBRARY" to "library"'
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(lExpected, oRule.violations)

    def test_rule_005(self):
        oRule = library.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '005')

        lExpected = []
        dViolation = utils.add_violation(26)
        dViolation['solution'] = 'Change "USE" to "use"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(27)
        dViolation['solution'] = 'Change "Use" to "use"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(30)
        dViolation['solution'] = 'Change "uSe" to "use"'
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(lExpected, oRule.violations)

    def test_rule_006(self):
        oRule = library.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '006')

        lExpected = []

        dViolation = utils.add_violation(27)
        dViolation['solution'] = 'Ensure there are only 1 space(s) between "Use" and "lib6.comp4.all"'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(30)
        dViolation['solution'] = 'Ensure there are only 1 space(s) between "uSe" and "lib6.comp5.all"'
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(lExpected, oRule.violations)

    def test_rule_007(self):
        oRule = library.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '007')

        dExpected = utils.add_violation_list([16,23,26,30])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        self.maxDiff = None
        oRule = library.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '008')

        lExpected = []

        dViolation = utils.add_violation(14)
        dViolation['action'] = 'insert'
        dViolation['iSpaces'] = '  '
        dViolation['solution'] = 'Indent 2 spaces'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(16)
        dViolation['action'] = 'insert'
        dViolation['iSpaces'] = '  '
        dViolation['solution'] = 'Indent 2 spaces'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(26)
        dViolation['action'] = 'insert'
        dViolation['iSpaces'] = '  '
        dViolation['solution'] = 'Indent 2 spaces'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(30)
        dViolation['action'] = 'change'
        dViolation['iSpaces'] = '  '
        dViolation['solution'] = 'Indent 2 spaces'
        lExpected.append(dViolation)

        dExpected = utils.add_violation_list([14,16,26,30])
        oRule.analyze(oFile)
        self.assertEqual(lExpected, oRule.violations)


    def test_rule_009(self):
        oRule = library.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'library')
        self.assertEqual(oRule.identifier, '009')
        lExpected = [{'lines':[{'number': 33}], 'indent': 1}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

