# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import interface_file_declaration as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import identifier_list, subtype_indication


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    interface_file_declaration ::=
        file identifier_list : subtype_indication
    """

    return oDataStructure.is_next_token("file")


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.file_keyword)

    identifier_list.classify_until([":"], oDataStructure, token.identifier)

    oDataStructure.replace_next_token_required(":", token.colon)

    subtype_indication.classify(oDataStructure)
