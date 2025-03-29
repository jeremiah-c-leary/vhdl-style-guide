# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import delay_mechanism as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import expression


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    delay_mechanism ::=
        transport
      | [ reject *time*_expression ] inertial
    """
    if oDataStructure.is_next_token_one_of(["transport", "reject", "inertial"]):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    if oDataStructure.is_next_token("transport"):
        oDataStructure.replace_next_token_with(token.transport_keyword)

    else:
        if oDataStructure.is_next_token("reject"):
            oDataStructure.replace_next_token_with(token.reject_keyword)
            expression.classify_until(["inertial"], oDataStructure)

        oDataStructure.replace_next_token_required("inertial", token.inertial_keyword)
