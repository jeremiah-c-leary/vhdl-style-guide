
from vsg.token import file_type_definition as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import type_mark


def detect(iToken, lObjects):
    '''
    file_type_definition ::=
        file of type_mark
    '''

    if utils.is_next_token('file', iToken, lObjects):
        return classify(iToken, lObjects)

    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('file', token.file_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_required('of', token.of_keyword, iCurrent, lObjects)

    iCurrent = type_mark.classify(iToken, lObjects)

    return iCurrent
