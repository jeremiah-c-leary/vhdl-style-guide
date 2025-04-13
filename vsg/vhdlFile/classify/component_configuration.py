# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import component_configuration as token
from vsg.vhdlFile.classify import (
    binding_indication,
    block_configuration,
    component_specification,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    component_configuration ::=
        for component_specification
            [ binding_indication ; ]
            { verification_unit_binding_indication ; }
            [ block_configuration ]
        end for ;
    """

    if oDataStructure.is_next_token("for"):
        oDataStructure.increment_seek_index()
        if component_specification.detect(oDataStructure):
            classify(oDataStructure)
            return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_required("for", token.for_keyword)

    component_specification.classify(oDataStructure)

    if binding_indication.detect(oDataStructure):
        oDataStructure.replace_next_token_required(";", token.binding_indication_semicolon)

    block_configuration.detect(oDataStructure)

    oDataStructure.replace_next_token_required("end", token.end_keyword)
    oDataStructure.replace_next_token_required("for", token.end_for_keyword)
    oDataStructure.replace_next_token_required(";", token.semicolon)
