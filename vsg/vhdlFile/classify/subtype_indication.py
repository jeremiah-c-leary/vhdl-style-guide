
from vsg.vhdlFile import utils

from vsg.token import subtype_indication as token

from vsg.vhdlFile.classify import constraint
from vsg.vhdlFile.classify import resolution_indication
from vsg.vhdlFile.classify import type_mark


def classify(iToken, lObjects):
    '''
    subtype_indication ::=
        [ resolution_indication ] type_mark [ constraint ]
    '''

    iCurrent = resolution_indication.detect(iToken, lObjects)
    iCurrent = utils.find_next_non_whitespace_token(iCurrent, lObjects)
    iCurrent = type_mark.classify(iCurrent, lObjects)
    iCurrent = constraint.detect(iCurrent, lObjects)
    return iCurrent
