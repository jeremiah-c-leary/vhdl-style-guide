# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import entity_aspect as token


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    entity_aspect ::=
        **entity** entity_name [ ( architecture_identifier ) ]
      | **configuration** configuration_name
      | **open**
    """

    if oDataStructure.is_next_token("open"):
        oDataStructure.replace_next_token_with(token.open_keyword)

    elif oDataStructure.is_next_token("configuration"):
        oDataStructure.replace_next_token_with(token.configuration_keyword)
        oDataStructure.replace_next_token_with(token.configuration_name)

    elif oDataStructure.is_next_token("entity"):
        oDataStructure.replace_next_token_with(token.entity_keyword)
        oDataStructure.replace_next_token_with(token.entity_name)

        if oDataStructure.is_next_token("("):
            oDataStructure.replace_next_token_with(token.open_parenthesis)
            oDataStructure.replace_next_token_with(token.architecture_identifier)
            oDataStructure.replace_next_token_required(")", token.close_parenthesis)
