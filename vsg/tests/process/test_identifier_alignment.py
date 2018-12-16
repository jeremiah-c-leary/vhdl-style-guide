
import os
import unittest

from vsg.rules import process
from vsg import vhdlFile
from vsg import line


class test_process_rules(unittest.TestCase):

    def setUp(self):
        self.sFileIdentifier = os.path.join(os.path.dirname(__file__),'identifier_alignment_input.vhd')
        self.oFileIdentifier = vhdlFile.vhdlFile(self.sFileIdentifier)

    def test_012(self):
        oRule = process.rule_031()
        oRule.analyze(self.oFileIdentifier)
        lExpected = ['22-32', '36-46']
        self.assertEqual(oRule.violations, lExpected)
