# -*- coding: utf-8 -*-

from vsg.token import package_header as token
from vsg.vhdlFile.classify import generic_clause, generic_map_aspect
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    package_header ::=
        [ generic_clause
        [ generic_map_aspect ; ] ]
    """

    if generic_clause.detect(oDataStructure):
        if generic_map_aspect.detect(oDataStructure):
            oDataStructure.assign_next_token_required(";", token.semicolon)
            return True
    return False
