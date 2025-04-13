# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import configuration_declaration as token
from vsg.vhdlFile.classify import block_configuration, configuration_declarative_part


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    configuration_declaration ::=
      configuration identifier of *entity*_name is
        configuration_declarative_part
        { verification_unit_binding_indication ; }
      block_configuration
      end [ configuration ] [ *configuration*_simple_name ] ;
    """

    if oDataStructure.is_next_token("configuration"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    classify_opening_declaration(oDataStructure)

    configuration_declarative_part.detect(oDataStructure)

    block_configuration.detect(oDataStructure)

    classify_closing_declaration(oDataStructure)


@decorators.print_classifier_debug_info(__name__)
def classify_opening_declaration(oDataStructure):
    oDataStructure.replace_next_token_with(token.configuration_keyword)
    oDataStructure.replace_next_token_with(token.identifier)
    oDataStructure.replace_next_token_required("of", token.of_keyword)
    oDataStructure.replace_next_token_with(token.entity_name)
    oDataStructure.replace_next_token_required("is", token.is_keyword)


@decorators.print_classifier_debug_info(__name__)
def classify_closing_declaration(oDataStructure):
    oDataStructure.replace_next_token_required("end", token.end_keyword)
    oDataStructure.replace_next_token_with_if("configuration", token.end_configuration_keyword)
    oDataStructure.replace_next_token_with_if_not(";", token.configuration_simple_name)
    oDataStructure.replace_next_token_required(";", token.semicolon)
