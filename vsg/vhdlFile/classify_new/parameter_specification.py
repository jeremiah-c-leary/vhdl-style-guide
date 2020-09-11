
from vsg import parser

from vsg.token import parameter_specification as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import discrete_range

'''
    parameter_specification ::=
        identifier in discrete_range
'''

def classify(iStart, iEnd, lObjects):
    bInFound = False
    for iToken in range(iStart, iEnd):
        if utils.is_item(lObjects, iToken):
            if utils.classify_token('in', token.in_keyword, iToken, lObjects):
                bInFound = True
            elif not bInFound:
                utils.assign_token(lObjects, iToken, token.identifier)
            else:
                utils.assign_token(lObjects, iToken, parser.todo)

    return iEnd


def classify_until(lUntils, iToken, lObjects):
    iCurrent = utils.assign_next_token(token.identifier, iToken, lObjects)
    iCurrent = utils.assign_next_token_required('in', token.in_keyword, iCurrent, lObjects)
    iCurrent = discrete_range.classify_until(lUntils, iCurrent, lObjects)    
    return iCurrent
