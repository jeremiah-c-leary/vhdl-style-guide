
from vsg import parser

from vsg.token import sensitivity_list as token

from vsg.vhdlFile import utils


def classify(iToken, lObjects):
    '''
    sensitivity_list ::=
        *signal*_name { , *signal*_element }
    '''
    iLast = 0
    while iLast != iToken:
        iToken = utils.find_next_token(iToken, lObjects)
        iLast = iToken
        # the sensitivity list ends in a close paranthesis, so we can use it to break out of this while loop
        if utils.object_value_is(lObjects, iToken, ')'):
            break
        elif utils.object_value_is(lObjects, iToken, ','):
            utils.assign_token(lObjects, iToken, token.comma)
        else:
            utils.assign_token(lObjects, iToken, parser.todo)
        iToken += 1
