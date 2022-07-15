import glob
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

    @classmethod
    def tearDownClass(cls):
        for sFilename in glob.glob('*_rules.rst'):
            try:
                os.remove(sFilename)
            except:
                pass

    def test_alias_declaration_rules_doc(self):

        lExpected, lActual = compare_files('alias_declaration')

        self.assertEqual(lExpected, lActual)

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

    def test_case_generate_alternative_rules_doc(self):

        lExpected, lActual = compare_files('case_generate_alternative')

        self.assertEqual(lExpected, lActual)

    def test_case_generate_statement_rules_doc(self):

        lExpected, lActual = compare_files('case_generate_statement')

        self.assertEqual(lExpected, lActual)

    def test_if_generate_statements_rules_doc(self):

        lExpected, lActual = compare_files('if_generate_statement')

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

    def test_element_association_rules_doc(self):

        lExpected, lActual = compare_files('element_association')

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

    def test_exponent_rules_doc(self):

        lExpected, lActual = compare_files('exponent')

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

    def test_if_rules_doc(self):

        lExpected, lActual = compare_files('if')

        self.assertEqual(lExpected, lActual)

    def test_instantiation_rules_doc(self):

        lExpected, lActual = compare_files('instantiation')

        self.assertEqual(lExpected, lActual)

    def test_length_rules_doc(self):

        lExpected, lActual = compare_files('length')

        self.assertEqual(lExpected, lActual)

    def test_library_rules_doc(self):

        lExpected, lActual = compare_files('library')

        self.assertEqual(lExpected, lActual)

    def test_logical_operator_rules_doc(self):

        lExpected, lActual = compare_files('logical_operator')

        self.assertEqual(lExpected, lActual)

    def test_loop_statement_rules_doc(self):

        lExpected, lActual = compare_files('loop_statement')

        self.assertEqual(lExpected, lActual)

    def test_package_rules_doc(self):

        lExpected, lActual = compare_files('package')

        self.assertEqual(lExpected, lActual)

    def test_package_body_rules_doc(self):

        lExpected, lActual = compare_files('package_body')

        self.assertEqual(lExpected, lActual)

    def test_port_rules_doc(self):

        lExpected, lActual = compare_files('port')

        self.assertEqual(lExpected, lActual)

    def test_port_map_rules_doc(self):

        lExpected, lActual = compare_files('port_map')

        self.assertEqual(lExpected, lActual)

    def test_procedure_rules_doc(self):

        lExpected, lActual = compare_files('procedure')

        self.assertEqual(lExpected, lActual)

    def test_procedure_call_rules_doc(self):

        lExpected, lActual = compare_files('procedure_call')

        self.assertEqual(lExpected, lActual)

    def test_process_rules_doc(self):

        lExpected, lActual = compare_files('process')

        self.assertEqual(lExpected, lActual)

    def test_range_rules_doc(self):

        lExpected, lActual = compare_files('range')

        self.assertEqual(lExpected, lActual)

    def test_record_type_definition_doc(self):

        lExpected, lActual = compare_files('record_type_definition')

        self.assertEqual(lExpected, lActual)

    def test_report_statement_rules_doc(self):

        lExpected, lActual = compare_files('report_statement')

        self.assertEqual(lExpected, lActual)

    def test_sequential_statement_rules_doc(self):

        lExpected, lActual = compare_files('sequential')

        self.assertEqual(lExpected, lActual)

    def test_signal_statement_rules_doc(self):

        lExpected, lActual = compare_files('signal')

        self.assertEqual(lExpected, lActual)

    def test_source_file_rules_doc(self):

        lExpected, lActual = compare_files('source_file')

        self.assertEqual(lExpected, lActual)

    def test_subprogram_body_rules_doc(self):

        lExpected, lActual = compare_files('subprogram_body')

        self.assertEqual(lExpected, lActual)

    def test_subtype_rules_doc(self):

        lExpected, lActual = compare_files('subtype')

        self.assertEqual(lExpected, lActual)

    def test_type_rules_doc(self):

        lExpected, lActual = compare_files('type')

        self.assertEqual(lExpected, lActual)

    def test_use_clause_rules_doc(self):

        lExpected, lActual = compare_files('use_clause')

        self.assertEqual(lExpected, lActual)

    def test_variable_rules_doc(self):

        lExpected, lActual = compare_files('variable')

        self.assertEqual(lExpected, lActual)

    def test_variable_assignment_rules_doc(self):

        lExpected, lActual = compare_files('variable_assignment')

        self.assertEqual(lExpected, lActual)

    def test_wait_rules_doc(self):

        lExpected, lActual = compare_files('wait')

        self.assertEqual(lExpected, lActual)

    def test_when_rules_doc(self):

        lExpected, lActual = compare_files('when')

        self.assertEqual(lExpected, lActual)

    def test_while_loop_rules_doc(self):

        lExpected, lActual = compare_files('while_loop')

        self.assertEqual(lExpected, lActual)

    def test_whitespace_rules_doc(self):

        lExpected, lActual = compare_files('whitespace')

        self.assertEqual(lExpected, lActual)

    def test_with_rules_doc(self):

        lExpected, lActual = compare_files('with')

        self.assertEqual(lExpected, lActual)


def compare_files(sRuleName):
    lExpected = []
    utils.read_file(os.path.join(sExpectedDir,f'{sRuleName}_rules.rst'), lExpected, bStrip=False)
    lActual = []
    utils.read_file(f'{sRuleName}_rules.rst', lActual, bStrip=False)

    return lExpected, lActual
