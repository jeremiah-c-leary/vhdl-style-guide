
from vsg.token import block_header as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import generic_clause
from vsg.vhdlFile.classify import generic_map_aspect
from vsg.vhdlFile.classify import port_clause
from vsg.vhdlFile.classify import port_map_aspect


def detect(iToken, lObjects):
    '''
    block_header ::=
        [ generic_clause
        [ generic_map_aspect ; ] ]
        [ port_clause
        [ port_map_aspect ; ] ]
    '''

    iCurrent = generic_clause.detect(iToken, lObjects)

    iLast = iCurrent
    iCurrent = generic_map_aspect.detect(iCurrent, lObjects)
    if iLast != iCurrent:
        iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    iCurrent = port_clause.detect(iCurrent, lObjects)

    iLast = iCurrent
    iCurrent = port_map_aspect.detect(iCurrent, lObjects)
    if iLast != iCurrent:
        iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
