
from vsg import parser

from vsg.token import range_constraint as token

from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    '''
    range_constraint ::=
        **range** range
    '''
    if utils.is_next_token('range', iToken, lObjects):
        return classify(iToken, lObjects)

    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required('range', token.range_keyword, iToken, lObjects)

    iParenCnt = 0
    while not utils.is_next_token_one_of([';', 'units', ':='], iCurrent, lObjects):
        if unmatched_closing_paren_found(iCurrent, lObjects, iParenCnt):
            break
        iCurrent = utils.assign_next_token(parser.todo, iCurrent, lObjects)

    return iCurrent


def unmatched_closing_paren_found(iCurrent, lObjects, iParenCnt):
    iCurrent = utils.find_next_token(iCurrent, lObjects)
    iParenCnt = utils.update_paren_counter(iCurrent, lObjects, iParenCnt)
    if iParenCnt == -1:
        return True
    return False
