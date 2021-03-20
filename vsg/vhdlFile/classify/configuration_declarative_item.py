
from vsg.vhdlFile.classify import attribute_specification
from vsg.vhdlFile.classify import group_declaration
from vsg.vhdlFile.classify import use_clause


def detect(iToken, lObjects):
    '''
    configuration_declarative_item ::=
        use_clause
      | attribute_specification
      | group_declaration
    '''

    iReturn = use_clause.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = attribute_specification.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = group_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    return iToken
