
from vsg.token import simple_release_assignment as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import force_mode


def detect(iToken, lObjects):
    '''
    simple_release_assignment ::=
        target <= release [ force_mode ] ;
    '''

    if utils.find_in_range('release', iToken, ';', lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_tokens_until('<=', token.target, iToken, lObjects)
    iCurrent = utils.assign_next_token_required('<=', token.assignment, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('release', token.release_keyword, iCurrent, lObjects)

    iCurrent = force_mode.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
