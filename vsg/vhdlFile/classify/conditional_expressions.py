# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import conditional_expressions as token
from vsg.vhdlFile.classify import condition, expression, utils


@decorators.print_classifier_debug_info(__name__)
def classify_until(lUntils, oDataStructure):
    """
    conditional_expressions ::=
        expression when condition
        { else expression when condition }
        [ else expression ]
    """

    lMyElseUntils = lUntils.copy()
    lMyElseUntils.append("else")
    lMyWhenUntils = lUntils.copy()
    lMyWhenUntils.append("when")

    expression.classify_until(["when"], oDataStructure)
    oDataStructure.replace_next_token_required("when", token.when_keyword)
    condition.classify_until(lMyElseUntils, oDataStructure)

    while oDataStructure.is_next_token("else"):
        oDataStructure.replace_next_token_required("else", token.else_keyword)
        expression.classify_until(lMyWhenUntils, oDataStructure)
        if oDataStructure.is_next_token_one_of(lUntils):
            break
        oDataStructure.replace_next_token_required("when", token.when_keyword)
        condition.classify_until(lMyElseUntils, oDataStructure)
