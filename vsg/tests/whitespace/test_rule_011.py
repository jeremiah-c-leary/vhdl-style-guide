
import os
import unittest

from vsg.rules import whitespace
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_011_test_input.vhd'))
lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_011_test_input.fixed.vhd'), lExpected)


class test_context_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_011(self):
        oRule = whitespace.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '011')

        lExpected = []
        lExpected.extend(range(23, 26))
        lExpected.extend(range(27, 30))
        lExpected.extend(range(31, 34))
        lExpected.extend(range(35, 38))
        lExpected.extend(range(39, 42))
        lExpected.extend(range(43, 46))
        lExpected.extend(range(47, 50))
        lExpected.extend(range(51, 54))
        lExpected.extend(range(55, 58))
        lExpected.extend(range(59, 62))
        lExpected.extend(range(63, 65))
        lExpected.extend(range(100, 105))
        lExpected.extend(range(106, 111))
        lExpected.extend(range(112, 117))

#        utils.print_objects(self.oFile,True)

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_011(self):
        oRule = whitespace.rule_011()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

