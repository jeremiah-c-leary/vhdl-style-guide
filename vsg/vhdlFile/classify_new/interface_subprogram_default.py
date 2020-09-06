
from vsg.token import interface_subprogram_default as token

from vsg.vhdlFile import utils


def classify(iToken, lObjects):
    '''
    interface_subprogram_default ::=
        *subprogram*_name | <> 
    '''
    iCurrent = utils.find_next_token(iToken, lObjects)
    if utils.object_value_is(lObjects, iCurrent, '<>'):
        return utils.classify_next_token(token.undefined_range, iToken, lObjects)
    return utils.classify_next_token(token.subprogram_name, iToken, lObjects)
