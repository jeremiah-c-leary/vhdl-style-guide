
from vsg.token import group_constituent_list as token

from vsg.vhdlFile import utils


def classify(iToken, lObjects):
    '''
    association_list ::=
        association_element { , association_element }
    '''
    iCurrent = utils.assign_next_token(token.group_constituent, iToken, lObjects)

    while utils.is_next_token(',', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required(',', token.comma, iCurrent, lObjects)
        iCurrent = utils.assign_next_token(token.group_constituent, iToken, lObjects)

    return iCurrent
