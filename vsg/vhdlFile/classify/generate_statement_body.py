# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import generate_statement_body as token
from vsg.vhdlFile.classify import block_declarative_part, concurrent_statement


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    generate_statement_body ::=
            [ block_declarative_part
        begin ]
            { concurrent_statement }
        [ end [ alternative_label ] ; ]
    """

    block_declarative_part.detect(oDataStructure)

    oDataStructure.replace_next_token_with_if("begin", token.begin_keyword)

    while not oDataStructure.is_next_token_one_of(["elsif", "else", "when", "end"]):
        if not concurrent_statement.detect(oDataStructure):
            break

    if oDataStructure.is_next_token("end"):
        if not oDataStructure.are_next_consecutive_tokens(["end", "generate"]):
            oDataStructure.replace_next_token_required("end", token.end_keyword)
            oDataStructure.replace_next_token_with_if_not(";", token.alternative_label)
            oDataStructure.replace_next_token_required(";", token.semicolon)
