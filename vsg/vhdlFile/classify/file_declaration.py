# -*- coding: utf-8 -*-

from vsg.token import file_declaration as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import (
    file_open_information,
    identifier_list,
    subtype_indication,
)
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    file_declaration ::=
        file identifier_list : subtype_indication [ file_open_information ] ;
    """

    if oDataStructure.is_next_token("file"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("file", token.file_keyword, iToken, lObjects)
    iCurrent = identifier_list.classify_until([":"], iCurrent, lObjects, token.identifier)
    iCurrent = utils.assign_next_token_required(":", token.colon, iCurrent, lObjects)

    iCurrent = subtype_indication.classify(iCurrent, lObjects)

    iCurrent = file_open_information.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent
