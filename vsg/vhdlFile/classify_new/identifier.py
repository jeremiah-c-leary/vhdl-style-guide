
from vsg.token import identifier as token

from vsg.vhdlFile import utils


'''
    identifier ::=
        basic_identifier | extended_identifier
'''

def classify(iToken, lObjects):
    return utils.assign_next_token(token.identifier, iToken, lObjects)
