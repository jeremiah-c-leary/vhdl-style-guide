
from vsg.vhdlFile.classify import interface_declaration


def classify(iToken, lObjects):
    '''
    interface_element ::=
        interface_declaration
    '''

    return interface_declaration.detect(iToken, lObjects)
