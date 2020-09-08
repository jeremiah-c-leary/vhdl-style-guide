
from vsg.vhdlFile.classify_new import block_statement
from vsg.vhdlFile.classify_new import component_instantiation_statement
from vsg.vhdlFile.classify_new import concurrent_assertion_statement
from vsg.vhdlFile.classify_new import concurrent_procedure_call_statement
from vsg.vhdlFile.classify_new import concurrent_signal_assignment_statement
from vsg.vhdlFile.classify_new import process_statement
from vsg.vhdlFile.classify_new import generate_statement

from vsg.vhdlFile import utils

'''
    concurrent_statement ::=
        block_statement
      | process_statement
      | concurrent_procedure_call_statement
      | concurrent_assertion_statement
      | concurrent_signal_assignment_statement
      | component_instantiation_statement
      | generate_statement
      | PSL_PSL_Directive
'''

def detect(iCurrent, lObjects):

    iReturn = process_statement.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    iReturn = block_statement.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    iReturn = generate_statement.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    iReturn = concurrent_assertion_statement.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    iReturn = concurrent_signal_assignment_statement.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    iReturn = concurrent_procedure_call_statement.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    iReturn = component_instantiation_statement.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    return iCurrent
