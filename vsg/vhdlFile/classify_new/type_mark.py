
from vsg.token import type_mark as token

from vsg.vhdlFile import utils

'''
    type_mark ::=
        *type*_name
      | *subtype*_name
'''


def classify(iToken, lObjects):
    return utils.assign_next_token(token.name, iToken, lObjects)
