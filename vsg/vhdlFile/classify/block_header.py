# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import block_header as token
from vsg.vhdlFile.classify import (
    generic_clause,
    generic_map_aspect,
    port_clause,
    port_map_aspect,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    block_header ::=
        [ generic_clause
        [ generic_map_aspect ; ] ]
        [ port_clause
        [ port_map_aspect ; ] ]
    """

    if generic_clause.detect(oDataStructure):
        generic_clause.classify(oDataStructure)

    if generic_map_aspect.detect(oDataStructure):
        oDataStructure.replace_next_token_required(";", token.semicolon)

    port_clause.detect(oDataStructure)

    if port_map_aspect.detect(oDataStructure):
        oDataStructure.replace_next_token_required(";", token.semicolon)
