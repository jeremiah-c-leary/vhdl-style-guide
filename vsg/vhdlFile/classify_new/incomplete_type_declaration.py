
from vsg.token import incomplete_type_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import identifier

'''
    incomplete_type_declaration ::=
        type identifier ;
'''


def detect(iToken, lObjects):
    if utils.is_next_token('type', iToken, lObjects):
        if utils.find_in_next_n_tokens(';', 3, iToken, lObjects):
            return classify(iToken, lObjects)
        else:
            return iToken
    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required('type', token.type_keyword, iToken, lObjects)
    iCurrent = identifier.classify(iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)
    return iCurrent
