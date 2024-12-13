# -*- coding: utf-8 -*-

# from vsg.vhdlFile import utils

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


def detect(iToken, lObjects):
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

    iReturn = wait_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = assertion_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = report_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = case_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = if_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = loop_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = variable_assignment_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = exit_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = signal_assignment_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = procedure_call_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = next_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = return_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = null_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn
    return iToken
