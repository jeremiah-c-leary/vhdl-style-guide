# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import package_header as token
from vsg.vhdlFile.classify import generic_clause, generic_map_aspect


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    package_header ::=
        [ generic_clause
        [ generic_map_aspect ; ] ]
    """

    if generic_clause.detect(oDataStructure):
        generic_clause.classify(oDataStructure)
        if generic_map_aspect.detect(oDataStructure):
            oDataStructure.replace_next_token_required(";", token.semicolon)
        return True
    return False
