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

    def test_case_rules_doc(self):

        lExpected, lActual = compare_files('case')

        self.assertEqual(lExpected, lActual)

    def test_comment_rules_doc(self):

        lExpected, lActual = compare_files('comment')

        self.assertEqual(lExpected, lActual)

    def test_component_rules_doc(self):

        lExpected, lActual = compare_files('component')

        self.assertEqual(lExpected, lActual)

    def test_concurrent_rules_doc(self):

        lExpected, lActual = compare_files('concurrent')

        self.assertEqual(lExpected, lActual)

    def test_constant_rules_doc(self):

        lExpected, lActual = compare_files('constant')

        self.assertEqual(lExpected, lActual)

    def test_context_rules_doc(self):

        lExpected, lActual = compare_files('context')

        self.assertEqual(lExpected, lActual)

    def test_context_ref_rules_doc(self):

        lExpected, lActual = compare_files('context_ref')

        self.assertEqual(lExpected, lActual)

    def test_entity_ref_rules_doc(self):

        lExpected, lActual = compare_files('entity')

        self.assertEqual(lExpected, lActual)

    def test_entity_specification_rules_doc(self):

        lExpected, lActual = compare_files('entity_specification')

        self.assertEqual(lExpected, lActual)

    def test_exit_statement_rules_doc(self):

        lExpected, lActual = compare_files('exit_statement')

        self.assertEqual(lExpected, lActual)

    def test_file_rules_doc(self):

        lExpected, lActual = compare_files('file')

        self.assertEqual(lExpected, lActual)

    def test_for_loop_rules_doc(self):

        lExpected, lActual = compare_files('for_loop')

        self.assertEqual(lExpected, lActual)

    def test_function_rules_doc(self):

        lExpected, lActual = compare_files('function')

        self.assertEqual(lExpected, lActual)

    def test_generate_rules_doc(self):

        lExpected, lActual = compare_files('generate')

        self.assertEqual(lExpected, lActual)

    def test_generic_rules_doc(self):

        lExpected, lActual = compare_files('generic')

        self.assertEqual(lExpected, lActual)

    def test_generic_map_rules_doc(self):

        lExpected, lActual = compare_files('generic_map')

        self.assertEqual(lExpected, lActual)



def compare_files(sRuleName):
    lExpected = []
    utils.read_file(os.path.join(sExpectedDir,f'{sRuleName}_rules.rst'), lExpected, bStrip=False)
    lActual = []
    utils.read_file(f'{sRuleName}_rules.rst', lActual, bStrip=False)

    return lExpected, lActual
