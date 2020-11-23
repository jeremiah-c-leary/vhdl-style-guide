
from vsg.vhdlFile.classify import interface_incomplete_type_declaration


def detect(iToken, lObjects):
    '''
    interface_type_declaration ::=
        interface_incomplete_type_declaration
    '''

    return interface_incomplete_type_declaration.detect(iToken, lObjects)
