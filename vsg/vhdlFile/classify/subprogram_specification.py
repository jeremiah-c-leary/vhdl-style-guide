
from vsg.vhdlFile.classify import procedure_specification
from vsg.vhdlFile.classify import function_specification


def detect(iCurrent, lObjects):
    '''
    subprogram_specification ::=
        procedure_specification
      | function_specification
    '''

    iReturn = procedure_specification.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    iReturn = function_specification.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    return iCurrent
