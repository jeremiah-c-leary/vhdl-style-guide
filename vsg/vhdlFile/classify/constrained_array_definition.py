# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import constrained_array_definition as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import index_constraint, subtype_indication


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    constrained_array_definition ::=
        array index_constraint of *element*_subtype_indication
    """

    if oDataStructure.is_next_token("array"):
        if not oDataStructure.does_string_exist_in_next_n_tokens("<>", 5):
            classify(oDataStructure)
            return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.array_keyword)

    index_constraint.classify(oDataStructure)

    oDataStructure.replace_next_token_required("of", token.of_keyword)

    subtype_indication.classify(oDataStructure)
