
from vsg.token import access_type_definition as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import subtype_indication

'''
    access_type_definition ::=
        access subtype_indication
'''


def detect(iToken, lObjects):
    if utils.is_next_token('access', iToken, lObjects):
        return classify(iToken, lObjects)

    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required('access', token.access_keyword, iToken, lObjects)
    iCurrent = utils.classify_subelement_until(';', subtype_indication, iCurrent, lObjects)
    return iCurrent
