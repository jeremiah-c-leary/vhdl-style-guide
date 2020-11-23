
from vsg.token import library_clause as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import logical_name_list


def detect(iToken, lObjects):
    '''
    library_clause ::=
        library logic_name_list ;
    '''
    if utils.is_next_token('library', iToken, lObjects):
        iCurrent = classify(iToken, lObjects)
        return iCurrent
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('library', token.keyword, iToken, lObjects)

    iCurrent = logical_name_list.classify_until([';'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
