
from vsg.token import record_element_constraint as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import element_constraint


def detect(iToken, lObjects):
    '''
    record_element_constraint ::=
        record_element_simple_name element_constraint
    '''
    if not utils.is_next_token('(', iToken, lObjects):
        iTemp = utils.find_next_token(iToken, lObjects) + 1
        if utils.is_next_token('(', iTemp, lObjects):
            return True
    return False


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token(token.record_element_simple_name, iToken, lObjects)
    iCurrent = element_constraint.detect(iCurrent, lObjects)

    return iCurrent
