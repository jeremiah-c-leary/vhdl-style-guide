
from vsg.vhdlFile import utils

from vsg.token import subtype_indication as token

from vsg.vhdlFile.classify import constraint
from vsg.vhdlFile.classify import resolution_indication


def classify(iToken, lObjects):
    '''
    subtype_indication ::=
        [ resolution_indication ] type_mark [ constraint ]
    '''

    iCurrent = resolution_indication.detect(iToken, lObjects)
    iCurrent = utils.find_next_non_whitespace_token(iCurrent, lObjects)
    iCurrent = utils.assign_next_token(token.type_mark, iCurrent, lObjects)
    iCurrent = constraint.detect(iCurrent, lObjects)
    return iCurrent
