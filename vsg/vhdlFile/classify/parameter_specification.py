# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import parameter_specification as token
from vsg.vhdlFile.classify import discrete_range


@decorators.print_classifier_debug_info(__name__)
def classify_until(lUntils, oDataStructure):
    """
    parameter_specification ::=
        identifier in discrete_range
    """

    oDataStructure.replace_next_token_with(token.identifier)
    oDataStructure.replace_next_token_required("in", token.in_keyword)

    discrete_range.classify_until(lUntils, oDataStructure)
