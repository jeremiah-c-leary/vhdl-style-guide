# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import attribute_specification as token
from vsg.vhdlFile.classify import entity_specification, expression


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    attribute_specification ::=
        attribute attribute_designator of entity_specification is expression ;
    """
    if oDataStructure.are_next_consecutive_tokens(["attribute", None, "of"]):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.attribute_keyword)
    oDataStructure.replace_next_token_with(token.attribute_designator)
    oDataStructure.replace_next_token_required("of", token.of_keyword)

    entity_specification.classify(oDataStructure)

    oDataStructure.replace_next_token_required("is", token.is_keyword)

    expression.classify_until([";"], oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
