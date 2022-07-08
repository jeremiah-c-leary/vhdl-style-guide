
from vsg.vhdlFile.classify import subtype_indication


def classify(iToken, lObjects):
    '''
    element_subtype_definition ::=
        subtype_indication
    '''

    return subtype_indication.classify(iToken, lObjects)
