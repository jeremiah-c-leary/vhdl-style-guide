
from vsg.vhdlFile.classify import concurrent_assertion_statement
from vsg.vhdlFile.classify import concurrent_procedure_call_statement
from vsg.vhdlFile.classify import process_statement


def detect(iToken, lObjects):
    '''
    entity_statement ::=
        concurrent_assertion_statement
      | *passive*_concurrent_procedure_call_statement
      | *passive*_process_statement
      | *PSL*_PSL_Directive
    '''

    iCurrent = process_statement.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = concurrent_assertion_statement.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = concurrent_procedure_call_statement.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    return iToken
