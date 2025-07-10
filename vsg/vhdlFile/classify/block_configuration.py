# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import block_configuration as token
from vsg.vhdlFile.classify import block_specification, configuration_item, use_clause


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    block_configuration ::=
        for block_specification
            { use_clause }
            { configuration_item }
        end for ;
    """

    if oDataStructure.is_next_token("for"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.for_keyword)

    block_specification.classify(oDataStructure)

    while use_clause.detect(oDataStructure):
        pass

    while configuration_item.detect(oDataStructure):
        pass

    oDataStructure.replace_next_token_required("end", token.end_keyword)
    oDataStructure.replace_next_token_required("for", token.end_for_keyword)
    oDataStructure.replace_next_token_with_if_not(";", token.unspecified)
    oDataStructure.replace_next_token_required(";", token.semicolon)
