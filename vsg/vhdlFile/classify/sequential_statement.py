# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import (
    assertion_statement,
    case_statement,
    exit_statement,
    if_statement,
    loop_statement,
    next_statement,
    null_statement,
    procedure_call_statement,
    report_statement,
    return_statement,
    signal_assignment_statement,
    variable_assignment_statement,
    wait_statement,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    sequential_statement ::=
        wait_statement
      | assertion_statement
      | report_statement
      | signal_assignment_statement
      | variable_assignment_statement
      | procedure_call_statement
      | if_statement
      | case_statement
      | loop_statement
      | next_statement
      | exit_statement
      | return_statement
      | null_statement
    """

    if wait_statement.detect(oDataStructure):
        return True

    if assertion_statement.detect(oDataStructure):
        return True

    if report_statement.detect(oDataStructure):
        return True

    if case_statement.detect(oDataStructure):
        return True

    if if_statement.detect(oDataStructure):
        return True

    if loop_statement.detect(oDataStructure):
        return True

    if variable_assignment_statement.detect(oDataStructure):
        return True

    if exit_statement.detect(oDataStructure):
        return True

    if signal_assignment_statement.detect(oDataStructure):
        return True

    if next_statement.detect(oDataStructure):
        return True

    if return_statement.detect(oDataStructure):
        return True

    if null_statement.detect(oDataStructure):
        return True

    return procedure_call_statement.detect(oDataStructure)
