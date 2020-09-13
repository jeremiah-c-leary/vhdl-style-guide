
from vsg.token import package_header as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import generic_clause
from vsg.vhdlFile.classify_new import generic_map_aspect


def detect(iToken, lObjects):
    '''
    package_header ::=
        [ generic_clause
        [ generic_map_aspect ; ] ]
    '''

    iReturn = generic_clause.detect(iToken, lObjects)

    iLast = iReturn
    iReturn = generic_map_aspect.detect(iReturn, lObjects)
    if iReturn != iLast:
        return utils.assign_next_token_required(';', token.semicolon, iReturn, lObjects)

    return iToken
