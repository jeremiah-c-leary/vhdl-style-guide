
from vsg.token import mode as token

from vsg.vhdlFile import utils


def classify(iToken, lObjects):
    '''
    mode ::=
        in | out | inout | buffer | linkage
    '''

    iCurrent = utils.assign_next_token_if('in', token.in_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if('out', token.out_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if('inout', token.inout_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if('buffer', token.buffer_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if('linkage', token.linkage_keyword, iCurrent, lObjects)

    return iCurrent
