
from vsg.vhdlFile.classify_new import block_statement
#from vsg.vhdlFile.classify import concurrent_procedure_call_statement
#from vsg.vhdlFile.classify import process_statement
#from vsg.vhdlFile.classify_new import generate_statement
#from vsg.vhdlFile.classify_new import concurrent_signal_assignment_statement
from vsg.vhdlFile.classify_new import concurrent_assertion_statement


def detect(iCurrent, lObjects):

    iReturn = block_statement.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    iReturn = concurrent_assertion_statement.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    return iCurrent
