
from vsg.token import interface_incomplete_type_declaration as token

from vsg.vhdlFile.classify_new import identifier

from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    '''
    interface_incomplete_type_declaration ::=
        type identifier
    '''
    iCurrent = utils.find_next_token(iToken, lObjects)
    if utils.object_value_is(lObjects, iCurrent, 'type'):
        return classify(iCurrent, lObjects)
    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_if('type', token.type_keyword, iToken, lObjects)
    iCurrent = identifier.classify(iCurrent, lObjects)
    return iCurrent
