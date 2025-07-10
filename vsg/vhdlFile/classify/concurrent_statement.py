# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import (
    block_statement,
    component_instantiation_statement,
    concurrent_assertion_statement,
    concurrent_procedure_call_statement,
    concurrent_signal_assignment_statement,
    generate_statement,
    process_statement,
    psl_psl_directive,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    concurrent_statement ::=
        block_statement
      | process_statement
      | concurrent_procedure_call_statement
      | concurrent_assertion_statement
      | concurrent_signal_assignment_statement
      | component_instantiation_statement
      | generate_statement
      | PSL_PSL_Directive
    """

    if process_statement.detect(oDataStructure):
        return True

    if block_statement.detect(oDataStructure):
        return True

    if generate_statement.detect(oDataStructure):
        return True

    if psl_psl_directive.detect(oDataStructure):
        return True

    if concurrent_assertion_statement.detect(oDataStructure):
        return True

    if concurrent_signal_assignment_statement.detect(oDataStructure):
        return True

    if concurrent_procedure_call_statement.detect(oDataStructure):
        return True

    return component_instantiation_statement.detect(oDataStructure)
