# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import file_declaration as token
from vsg.vhdlFile.classify import (
    file_open_information,
    identifier_list,
    subtype_indication,
)


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
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.file_keyword)
    identifier_list.classify_until([":"], oDataStructure, token.identifier)
    oDataStructure.replace_next_token_required(":", token.colon)

    subtype_indication.classify(oDataStructure)

    file_open_information.detect(oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
