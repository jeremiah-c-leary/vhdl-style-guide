# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import (
    block_statement,
    component_instantiation_statement,
    concurrent_assertion_statement,
    concurrent_procedure_call_statement,
    concurrent_signal_assignment_statement,
    generate_statement,
    process_statement,
)


def detect(iToken, lObjects):
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

    iCurrent = process_statement.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = block_statement.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = generate_statement.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = concurrent_assertion_statement.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = concurrent_signal_assignment_statement.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = concurrent_procedure_call_statement.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = component_instantiation_statement.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    return iToken
