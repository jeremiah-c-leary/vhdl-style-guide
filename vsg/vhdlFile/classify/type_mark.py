
from vsg.token import type_mark as token

from vsg.vhdlFile import utils

from vsg import parser


def classify(iToken, lObjects):
    '''
    type_mark ::=
        *type*_name
      | *subtype*_name
    '''
    iCurrent = utils.assign_next_token(token.name, iToken, lObjects)

    if utils.is_next_token("'", iCurrent, lObjects):
        iCurrent = utils.assign_next_token(token.tic, iCurrent, lObjects)
        iCurrent = utils.assign_next_token(token.attribute, iCurrent, lObjects)

    return iCurrent
