# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import selected_expressions as token
from vsg.vhdlFile.classify import choices, expression


@decorators.print_classifier_debug_info(__name__)
def classify_until(lUntils, oDataStructure):
    """
    selected_expressions ::=
        { expression when choices , }
        expression when choices
    """

    lMyUntils = lUntils
    lMyUntils.append(",")

    expression.classify_until(["when"], oDataStructure)

    oDataStructure.replace_next_token_required("when", token.when_keyword)

    choices.classify_until(lMyUntils, oDataStructure)

    while oDataStructure.is_next_token(","):
        oDataStructure.replace_next_token_required(",", token.comma)

        expression.classify_until(["when"], oDataStructure)

        oDataStructure.replace_next_token_required("when", token.when_keyword)

        choices.classify_until(lMyUntils, oDataStructure)
