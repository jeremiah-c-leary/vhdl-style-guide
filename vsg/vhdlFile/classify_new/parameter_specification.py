
from vsg import parser
from vsg.token import parameter_specification as token

from vsg.vhdlFile import utils


def classify(iStart, iEnd, lObjects):
    '''
    logical_name_list ::=
        logical_name { , logical_name }
    '''
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
