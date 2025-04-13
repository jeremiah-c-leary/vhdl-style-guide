# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import subprogram_declaration as token
from vsg.vhdlFile.classify import subprogram_specification


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    subprogram_declaration ::=
        subprogram_specification ;
    """

    if subprogram_specification.detect(oDataStructure):
        if oDataStructure.is_next_token(";"):
            oDataStructure.replace_next_token_with(token.semicolon)
        return True
    return False
