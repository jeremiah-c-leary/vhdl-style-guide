import os

import unittest
from vsg import vhdlFile
from vsg.tests import utils

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','code_tags','code_tag_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testCodeTags(unittest.TestCase):

    def test_hasCodeTag(self):
        lExpected = []
        lExpected.extend(range(2, 6))
        lExpected.extend(range(10, 18))
        lExpected.extend(range(20, 33))

        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.hasCodeTag:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_library_008_tag(self):
        lExpected = []
        lExpected.extend(range(2, 6))

        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.hasCodeTag and 'vsg_off' in oLine.codeTags:
                if 'library_008' in oLine.codeTags['vsg_off']:
                    lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_empty_code_tags(self):
        lExpected = []
        lExpected.extend(range(10, 18))

        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.hasCodeTag and 'vsg_off' in oLine.codeTags:
                if len(oLine.codeTags['vsg_off']) == 0:
                    lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_library_001_tag(self):
        lExpected = []
        lExpected.extend(range(20, 24))
        lExpected.extend(range(30, 33))

        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.hasCodeTag and 'vsg_off' in oLine.codeTags:
                if 'library_001' in oLine.codeTags['vsg_off']:
                    lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)


    def test_process_001_tag(self):
        lExpected = []
        lExpected.extend(range(20, 29))

        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.hasCodeTag and 'vsg_off' in oLine.codeTags:
                if 'process_001' in oLine.codeTags['vsg_off']:
                    lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_case_001_tag(self):
        lExpected = []
        lExpected.extend(range(26, 33))

        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.hasCodeTag and 'vsg_off' in oLine.codeTags:
                if 'case_001' in oLine.codeTags['vsg_off']:
                    lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)
