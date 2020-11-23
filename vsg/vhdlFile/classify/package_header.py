
from vsg.token import package_header as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import generic_clause
from vsg.vhdlFile.classify import generic_map_aspect


def detect(iToken, lObjects):
    '''
    package_header ::=
        [ generic_clause
        [ generic_map_aspect ; ] ]
    '''

    iCurrent = generic_clause.detect(iToken, lObjects)

    iLast = iCurrent
    iCurrent = generic_map_aspect.detect(iCurrent, lObjects)
    if iCurrent != iLast:
        return utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iToken
