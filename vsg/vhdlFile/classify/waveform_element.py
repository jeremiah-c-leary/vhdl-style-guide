# -*- coding: utf-8 -*-

from vsg.token import waveform_element as token
from vsg.vhdlFile.classify import expression
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def classify_until(lUntils, oDataStructure):
    """
    waveform_element ::=
        *value*_expression [ after *time*_expression ]
      | null [ after *time*_expression ]
    """

    if oDataStructure.is_next_token("null"):
        oDataStructure.replace_next_token_with(token.null_keyword)
    else:
        lMyUntils = lUntils
        lMyUntils.append("after")
        expression.classify_until(lMyUntils, oDataStructure)

    if oDataStructure.is_next_token("after"):
        oDataStructure.replace_next_token_with(token.after_keyword)
        expression.classify_until(lUntils, oDataStructure)
