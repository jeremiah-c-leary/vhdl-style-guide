
from vsg.vhdlFile.classify_new import concurrent_assertion_statement
from vsg.vhdlFile.classify_new import concurrent_procedure_call_statement
from vsg.vhdlFile.classify_new import process_statement

from vsg.vhdlFile import utils

'''
    entity_statement ::=
        concurrent_assertion_statement
      | *passive*_concurrent_procedure_call_statement
      | *passive*_process_statement
      | *PSL*_PSL_Directive
'''

def detect(iToken, lObjects):

    iReturn = process_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = concurrent_assertion_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = concurrent_procedure_call_statement.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    return iToken
