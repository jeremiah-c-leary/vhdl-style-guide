# -*- coding: utf-8 -*-

from vsg.token import access_type_definition as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import subtype_indication


def detect(oDataStructure):
    """
    access_type_definition ::=
        access subtype_indication
    """

    if oDataStructure.is_next_token("access"):
        classify(oDataStructure)
        return True
    return False


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("access", token.access_keyword, iToken, lObjects)

    iCurrent = subtype_indication.classify(iCurrent, lObjects)

    return iCurrent
