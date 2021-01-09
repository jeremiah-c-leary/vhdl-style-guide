
from vsg.token import file_open_information as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import file_logical_name


def detect(iToken, lObjects):
    '''
    file_open_information ::=
        [ open *file_open_kind*_expression ] is file_logical_name
    '''

    if utils.is_next_token_one_of(['open', 'is'], iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = iToken

    if utils.is_next_token('open', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('open', token.open_keyword, iCurrent, lObjects)
        iCurrent = utils.assign_next_token(token.file_open_kind_expression, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('is', token.is_keyword, iCurrent, lObjects)

    iCurrent = file_logical_name.classify(iCurrent, lObjects)

    return iCurrent
