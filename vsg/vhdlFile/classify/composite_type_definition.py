

from vsg.vhdlFile.classify import array_type_definition
from vsg.vhdlFile.classify import record_type_definition


def detect(iToken, lObjects):
    '''
    composite_type_definition ::=
        array_type_definition
      | record_type_definition
    '''

    iCurrent = array_type_definition.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = record_type_definition.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    return iToken
