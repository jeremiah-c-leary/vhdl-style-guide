
from vsg.token import interface_file_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import identifier_list
from vsg.vhdlFile.classify_new import subtype_indication


def detect(iToken, lObjects):
    '''
    interface_file_declaration ::=
        file identifier_list : subtype_indication
    '''

    if utils.is_next_token('file', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('file', token.file_keyword, iToken, lObjects)

    iCurrent = identifier_list.classify_until([':'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(':', token.colon, iCurrent, lObjects)

    iCurrent = subtype_indication.classify_until([')', ';'], iCurrent, lObjects)

    return iCurrent
