# -*- coding: utf-8 -*-

from vsg.token import block_configuration as token
from vsg.vhdlFile.classify import block_specification, configuration_item, use_clause


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


def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.for_keyword)

    block_specification.classify(oDataStructure)

    use_clause.detect(oDataStructure)
    configuration_item.detect(oDataStructure)

    oDataStructure.replace_next_token_required("end", token.end_keyword, iCurrent, lObjects)
    oDataStructure.replace_next_token_required("for", token.end_for_keyword, iCurrent, lObjects)
    oDataStructure.replace_next_token_with_if_not(";", token.unspecified, iCurrent, lObjects)
    oDataStructure.replace_next_token_required(";", token.semicolon, iCurrent, lObjects)
