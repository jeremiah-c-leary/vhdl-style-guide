
from vsg.token import array_constraint as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import array_element_constraint
from vsg.vhdlFile.classify import index_constraint


def detect(iToken, lObjects):
    '''
    array_constraint ::=
        index_constraint [ array_element_constraint ]
      | ( open ) [ array_element_constraint ]

    '''
    if open_detected(iToken, lObjects):
        return classify(iToken, lObjects)
    if index_constraint.detect(iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.find_next_token(iToken, lObjects)
    if utils.is_next_token('open', iCurrent + 1, lObjects):
        iCurrent = utils.assign_next_token_required('(', token.open_parenthesis, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required('open', token.open_keyword, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required(')', token.close_parenthesis, iCurrent, lObjects)
    else:
        iCurrent = index_constraint.classify(iCurrent, lObjects)

    iCurrent = array_element_constraint.detect(iCurrent, lObjects)

    return iCurrent


def open_detected(iToken, lObjects):
    if utils.is_next_token('(', iToken, lObjects):
        if utils.find_in_next_n_tokens('open', 2, iToken, lObjects):
            return True
    return False
