
from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import interface_function_specification
from vsg.vhdlFile.classify import interface_procedure_specification

'''
    interface_subprogram_specification ::=
        interface_procedure_specification
      | interface_function_specification
'''

def detect(iToken, lObjects):

    iCurrent = interface_procedure_specification.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = interface_function_specification.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    return iToken
