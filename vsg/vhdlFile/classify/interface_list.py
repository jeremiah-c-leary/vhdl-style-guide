
from vsg.token import interface_list as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import interface_element


def classify(iToken, lObjects):
    '''
    interface_list ::=
        interface_element { ; interface_element }
    '''

    iCurrent = interface_element.classify(iToken, lObjects)

    while utils.is_next_token(';', iCurrent, lObjects):
         iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)
         iCurrent = interface_element.classify(iToken, lObjects)

    return iCurrent
