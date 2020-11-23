

from vsg.vhdlFile.classify import full_type_declaration
from vsg.vhdlFile.classify import incomplete_type_declaration


def detect(iToken, lObjects):
    '''
    type_declaration ::=
        full_type_declaration
      | incomplete_type_declaration
    '''

    iReturn = full_type_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = incomplete_type_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    return iToken
