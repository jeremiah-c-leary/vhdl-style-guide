
from vsg import parser

from vsg.token import range_constraint as token

from vsg.vhdlFile import utils

'''
    range_constraint ::=
        **range** range
'''


def detect(iToken, lObjects):
    if utils.is_next_token('range', iToken, lObjects):
        return classify(iToken, lObjects)

    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required('range', token.range_keyword, iToken, lObjects)

    while not utils.is_next_token(';', iCurrent, lObjects):
        iCurrent = utils.assign_next_token(parser.todo, iCurrent, lObjects)
    
    return iCurrent
