
from vsg.token import association_list as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import association_element


def classify(iToken, lObjects):
    '''
    association_list ::=
        association_element { , association_element }
    '''
    iCurrent = association_element.detect(iToken, lObjects)

    while utils.is_next_token(',', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required(',', token.comma, iCurrent, lObjects)
        iCurrent = association_element.detect(iCurrent, lObjects)

    return iCurrent
