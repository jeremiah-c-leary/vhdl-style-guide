
from vsg.token import access_type_definition as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import subtype_indication


def detect(iToken, lObjects):
    '''
    access_type_definition ::=
        access subtype_indication
    '''

    if utils.is_next_token('access', iToken, lObjects):
        return classify(iToken, lObjects)

    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('access', token.access_keyword, iToken, lObjects)

    iCurrent = subtype_indication.classify_until([';'], iCurrent, lObjects)

    return iCurrent
