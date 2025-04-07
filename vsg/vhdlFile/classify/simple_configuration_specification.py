# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import simple_configuration_specification as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import binding_indication, component_specification


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    simple_configuration_specification ::=
        **for** component_specification binding_indication ;
        [ **end** **for** ; ]
    """
    if oDataStructure.is_next_token("for"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.for_keyword)

    component_specification.classify(oDataStructure)

    binding_indication.classify(oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)

    if oDataStructure.is_next_token("end"):
        oDataStructure.replace_next_token_with(token.end_keyword)
        oDataStructure.replace_next_token_required("for", token.end_for_keyword)
        oDataStructure.replace_next_token_required(";", token.semicolon)
