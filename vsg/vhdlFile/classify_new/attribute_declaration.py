
from vsg.token import attribute_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import type_mark

'''
    attribute_declaration ::=
        attribute identifier : type_mark ;
'''


def detect(iToken, lObjects):

    if utils.is_next_token('attribute', iToken, lObjects):
        return classify(iToken, lObjects)    

    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required('attribute', token.attribute_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token(token.identifier, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(':', token.colon, iCurrent, lObjects)
    iCurrent = type_mark.classify(iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)
    return iCurrent 
