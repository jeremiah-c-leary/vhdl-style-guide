# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import instantiated_unit as token


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    instantiated_unit ::=
        [ component ] component_name
      | entity entity_name [ ( *architecture*_identifier ) ]
      | configuration configuration_name
    """

    if oDataStructure.is_next_seek_token_one_of(["component", "entity", "configuration"]):
        return True
    if oDataStructure.does_string_exist_in_next_n_tokens(";", 2):
        return True
    # Check if this is a signal assignment
    if oDataStructure.does_string_exist_before_string("<=", ";"):
        return False
    if oDataStructure.does_string_exist_before_string("generate", ";"):
        return False
    return True


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    if oDataStructure.is_next_token("component"):
        oDataStructure.replace_next_token_with(token.component_keyword)
        oDataStructure.replace_next_token_with(token.component_name)

    elif oDataStructure.is_next_token("configuration"):
        oDataStructure.replace_next_token_with(token.configuration_keyword)
        oDataStructure.replace_next_token_with(token.configuration_name)

    elif oDataStructure.is_next_token("entity"):
        oDataStructure.replace_next_token_with(token.entity_keyword)

        classify_entity_name(oDataStructure)

        if oDataStructure.is_next_token("("):
            oDataStructure.replace_next_token_with(token.open_parenthesis)
            oDataStructure.replace_next_token_with_if_not(")", token.architecture_identifier)
            oDataStructure.replace_next_token_required(")", token.close_parenthesis)
    else:
        oDataStructure.replace_next_token_with(token.component_name)


@decorators.print_classifier_debug_info(__name__)
def classify_entity_name(oDataStructure):
    oDataStructure.advance_to_next_token()
    sTokenValue = oDataStructure.get_current_token_value()
    if "." in sTokenValue:
        lTokenValue = sTokenValue.split(".")
        oDataStructure.lAllObjects[oDataStructure.iCurrent] = token.library_name(lTokenValue[0])
        oDataStructure.lAllObjects.insert(oDataStructure.iCurrent + 1, token.dot("."))
        oDataStructure.lAllObjects.insert(oDataStructure.iCurrent + 2, token.entity_name(lTokenValue[1]))
        oDataStructure.iCurrent += 2
        oDataStructure.iEndIndex += 2
    else:
        oDataStructure.replace_next_token_with(token.entity_name)
