

from vsg.vhdlFile.classify import enumeration_type_definition
from vsg.vhdlFile.classify import physical_type_definition
from vsg.vhdlFile.classify import integer_type_definition


def detect(iToken, lObjects):
    '''
    scalar_type_definition ::=
        enumeration_type_definition
      | integer_type_definition
      | floating_type_definition
      | physical_type_definition

    NOTE:  floating and physical types are not parsed yet.
           They are very similar to integer types, and will hopefully not be required.
    '''

    iReturn = physical_type_definition.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = enumeration_type_definition.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = integer_type_definition.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    return iToken
