
from vsg import parser
from vsg.token import logical_name_list as token

from vsg.vhdlFile import utils


def classify(iStart, iEnd, lObjects):
    '''
    logical_name_list ::=
        logical_name { , logical_name }
    '''
    for iToken in range(iStart, iEnd):
        if utils.is_item(lObjects, iToken):
            if utils.classify_token(',', token.comma, iToken, lObjects):
                continue
            else:
                utils.assign_token(lObjects, iToken, token.logical_name)
    return iEnd
