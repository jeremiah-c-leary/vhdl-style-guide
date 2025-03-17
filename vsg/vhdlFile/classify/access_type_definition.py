# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import access_type_definition as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import subtype_indication


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    access_type_definition ::=
        access subtype_indication
    """

    if oDataStructure.is_next_token("access"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("access", token.access_keyword, iToken, lObjects)

    iCurrent = subtype_indication.classify(iCurrent, lObjects)

    return iCurrent
