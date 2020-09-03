
from vsg.token import association_list as token

from vsg.vhdlFile.classify_new import association_element

from vsg.vhdlFile import utils


def classify(iCurrent, lObjects):
    '''
    association_list ::=
        association_element { , association_element }
    '''
    iLast = 0
    iToken = iCurrent
    while iLast != iToken:
        iLast = iToken
        iToken = association_element.detect(iToken, lObjects)
        iToken = utils.find_next_token(iToken, lObjects)
        if utils.object_value_is(lObjects, iToken, ','):
            utils.assign_token(lObjects, iToken, token.comma)
            iToken += 1
        # All association lists end in a close paranthesis, so we can use it to break out of this while loop
        if utils.object_value_is(lObjects, iToken, ')'):
            break

    return iToken
