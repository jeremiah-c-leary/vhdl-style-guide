
from vsg.token import interface_list as token

from vsg.vhdlFile.classify_new import interface_element

from vsg.vhdlFile import utils


def classify(iToken, lObjects):
    '''
    interface_list ::=
        interface_element { ; interface_element }
    '''
    iLast = 0
    iCurrent = iToken
    while iLast != iCurrent:
        iLast = iCurrent
        iCurrent = interface_element.classify(iCurrent, lObjects)
        iCurrent = utils.classify_next_token_if(';', token.semicolon, iCurrent, lObjects)
        # All interface lists end in a close paranthesis, so we can use it to break out of this while loop
        if utils.is_next_token(')', iCurrent, lObjects):
            return iCurrent

    return iCurrent
