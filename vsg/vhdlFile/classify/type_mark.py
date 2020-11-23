
from vsg.token import type_mark as token

from vsg.vhdlFile import utils


def classify(iToken, lObjects):
    '''
    type_mark ::=
        *type*_name
      | *subtype*_name
    '''

    return utils.assign_next_token(token.name, iToken, lObjects)
