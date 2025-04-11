# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import element_declaration as token
from vsg.vhdlFile.classify import element_subtype_definition, identifier_list


def detect(oDataStructure):
    """
    element_declaration ::=
        identifier_list : element_subtype_definition ;
    """

    if oDataStructure.does_string_exist_before_string(":", ";"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):

    identifier_list.classify_until([":"], oDataStructure)

    oDataStructure.replace_next_token_required(":", token.colon)

    element_subtype_definition.classify(oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
