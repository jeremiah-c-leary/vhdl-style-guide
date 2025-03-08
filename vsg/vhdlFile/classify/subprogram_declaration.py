# -*- coding: utf-8 -*-

from vsg.token import subprogram_declaration as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import subprogram_specification
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    subprogram_declaration ::=
        subprogram_specification ;
    """

    if subprogram_specification.detect(oDataStructure):
        oDataStructure.replace_next_token_required(";", token.semicolon)
        return True
    return False
