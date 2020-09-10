
from vsg.token import interface_list as token

from vsg.vhdlFile.classify_new import interface_element

from vsg.vhdlFile import utils


def classify(iToken, lObjects):
    '''
    interface_list ::=
        interface_element { ; interface_element }
    '''
    iCurrent = iToken
    iOpenParenthesis = 0
    iCloseParenthesis = 0
    # All interface lists end in a close paranthesis, so we can use it to break out of this while loop
    #while not(iOpenParenthesis == iCloseParenthesis and utils.is_next_token(')', iCurrent,lObjects)):
    while True:
        if utils.is_next_token(';', iCurrent, lObjects):            
            iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)
            iOpenparenthesis = 0
            iCloseparenthesis = 0
            continue
        if iOpenParenthesis == iCloseParenthesis:
            if utils.is_next_token(')', iCurrent, lObjects):
                return iCurrent       
        if utils.is_next_token('(', iCurrent, lObjects):
            iOpenParenthesis += 1
        if utils.is_next_token(')', iCurrent, lObjects):
            iCloseParenthesis += 1
        iCurrent = interface_element.classify(iCurrent, lObjects)

   
    #    if utils.is_next_token(')', iCurrent, lObjects):
    #        if iOpenParenthesis == iCloseParenthesis:
    #            return iCurrent

    return iCurrent
