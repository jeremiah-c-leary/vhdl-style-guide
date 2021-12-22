import os
import unittest

from vsg import __rule_doc_gen__

from vsg.tests import utils

sExpectedDir = 'docs'
sResultsDir = os.path.dirname(__file__)


class testDocGen(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        __rule_doc_gen__.create_rule_documentation()

    def test_after_rules_doc(self):

        lExpected, lActual = compare_files('after')

        self.assertEqual(lExpected, lActual)

    def test_architecture_rules_doc(self):

        lExpected, lActual = compare_files('architecture')

        self.assertEqual(lExpected, lActual)

    def test_assert_rules_doc(self):

        lExpected, lActual = compare_files('assert')

        self.assertEqual(lExpected, lActual)

    def test_attribute_rules_doc(self):

        lExpected, lActual = compare_files('attribute')

        self.assertEqual(lExpected, lActual)

    def test_attribute_declaration_rules_doc(self):

        lExpected, lActual = compare_files('attribute_declaration')

        self.assertEqual(lExpected, lActual)

    def test_attribute_specification_rules_doc(self):

        lExpected, lActual = compare_files('attribute_specification')

        self.assertEqual(lExpected, lActual)

    def test_block_rules_doc(self):

        lExpected, lActual = compare_files('block')

        self.assertEqual(lExpected, lActual)

    def test_block_comment_rules_doc(self):

        lExpected, lActual = compare_files('block_comment')

        self.assertEqual(lExpected, lActual)





def compare_files(sRuleName):
    lExpected = []
    utils.read_file(os.path.join(sExpectedDir,f'{sRuleName}_rules.rst'), lExpected, bStrip=False)
    lActual = []
    utils.read_file(f'{sRuleName}_rules.rst', lActual, bStrip=False)

    return lExpected, lActual
