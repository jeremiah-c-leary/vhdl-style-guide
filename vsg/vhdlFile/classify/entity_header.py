

from vsg.vhdlFile.classify import generic_clause
from vsg.vhdlFile.classify import port_clause


def detect(iToken, lObjects):
    '''
    entity_header ::=
        [ *formal*_generic_clause ]
        [ *formal*_port_clause ]
    '''

    iReturn = generic_clause.detect(iToken, lObjects)

    iReturn = port_clause.detect(iReturn, lObjects)

    return iReturn
