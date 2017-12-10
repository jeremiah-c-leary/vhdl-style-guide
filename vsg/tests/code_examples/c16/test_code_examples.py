import os
import sys
import unittest


from vsg import vhdlFile
from vsg import rule_list
from vsg.tests import utils

oBaudGen = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'BaudGen.vhd'))

class testCodeExample(unittest.TestCase):

    def test_baudgen(self):
        oRuleList = rule_list.list(oBaudGen)
        oRuleList.fix()
        lExpected = ['']
        utils.read_file(os.path.join(os.path.dirname(__file__),'BaudGen.fixed.vhd'), lExpected)
        for iLineNumber, sLine in enumerate(lExpected):
            self.assertEqual(oBaudGen.lines[iLineNumber].line, sLine)

