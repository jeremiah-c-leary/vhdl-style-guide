
from vsg.token import record_constraint as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import record_element_constraint


def detect(iToken, lObjects):
    '''
    record_constraint ::=
        ( record_element_constraint { , record_element_constraint } )
    '''
    if utils.is_next_token('(', iToken, lObjects):
        iTemp = utils.find_next_token(iToken, lObjects) + 1
        if record_element_constraint.detect(iTemp, lObjects):
            return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('(', token.open_parenthesis, iToken, lObjects)

    while not utils.is_next_token(')', iCurrent, lObjects):
        iCurrent = record_element_constraint.classify(iCurrent, lObjects)
        iCurrent = utils.assign_next_token_if(',', token.comma, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(')', token.close_parenthesis, iCurrent, lObjects)

    return iCurrent
