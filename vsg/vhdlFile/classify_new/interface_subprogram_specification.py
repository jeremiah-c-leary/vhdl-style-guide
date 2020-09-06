
from vsg.vhdlFile.classify_new import interface_procedure_specification
from vsg.vhdlFile.classify_new import interface_function_specification

from vsg.vhdlFile import utils

'''
    interface_subprogram_specification ::=
        interface_procedure_specification
      | interface_function_specification
'''

def detect(iCurrent, lObjects):

    iReturn = interface_procedure_specification.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    iReturn = interface_function_specification.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    return iCurrent
