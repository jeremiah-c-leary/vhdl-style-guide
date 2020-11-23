
#from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import assertion_statement
from vsg.vhdlFile.classify import case_statement
from vsg.vhdlFile.classify import exit_statement
from vsg.vhdlFile.classify import if_statement
from vsg.vhdlFile.classify import loop_statement
from vsg.vhdlFile.classify import next_statement
from vsg.vhdlFile.classify import null_statement
from vsg.vhdlFile.classify import procedure_call_statement
from vsg.vhdlFile.classify import report_statement
from vsg.vhdlFile.classify import return_statement
from vsg.vhdlFile.classify import signal_assignment_statement
from vsg.vhdlFile.classify import variable_assignment_statement
from vsg.vhdlFile.classify import wait_statement


def detect(iToken, lObjects):
    '''
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
    '''

#    print('--> checking wait_statement')
    iReturn = wait_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

#    print('--> checking assertion_statement')
    iReturn = assertion_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

#    print('--> checking report_statement')
    iReturn = report_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

#    print('--> checking case_statement')
    iReturn = case_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

#    print('--> checking if_statement')
    iReturn = if_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

#    print('--> checking loop_statement')
    iReturn = loop_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn
#    print('--> checking signal_assignment')
    iReturn = signal_assignment_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

#    print('--> checking variable_assignment')
    iReturn = variable_assignment_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

#    print('--> checking procedure_call_statement')
    iReturn = procedure_call_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

#    print('--> checking next_statement')
    iReturn = next_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

#    print('--> checking exit_statement')
    iReturn = exit_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

#    print('--> checking return_statement')
    iReturn = return_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

#    print('--> checking null_statement')
    iReturn = null_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn
#    print('<-- Returning')
#    utils.print_next_token(iToken, lObjects)
    return iToken
