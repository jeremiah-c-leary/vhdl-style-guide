# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import component_declaration as token
from vsg.vhdlFile.classify import generic_clause, port_clause


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    component_declaration ::=
        component identifier [ is ]
            [ *local*_generic_clause ]
            [ *local*_port_clause ]
        end component [ *component*_simple_name ] ;
    """

    if oDataStructure.is_next_token("component"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.component_keyword)
    oDataStructure.replace_next_token_with(token.identifier)
    oDataStructure.replace_next_token_with_if("is", token.is_keyword)

    if generic_clause.detect(oDataStructure):
        generic_clause.classify(oDataStructure)

    if port_clause.detect(oDataStructure):
        port_clause.classify(oDataStructure)

    oDataStructure.replace_next_token_required("end", token.end_keyword)
    oDataStructure.replace_next_token_required("component", token.end_component_keyword)
    oDataStructure.replace_next_token_with_if_not(";", token.component_simple_name)
    oDataStructure.replace_next_token_required(";", token.semicolon)
