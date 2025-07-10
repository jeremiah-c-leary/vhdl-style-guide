# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import choices as token
from vsg.vhdlFile.classify import choice


@decorators.print_classifier_debug_info(__name__)
def classify_until(lUntils, oDataStructure):
    """
    choices ::=
        choice { | choice }
    """

    lMyUntils = lUntils
    lMyUntils.append("|")

    choice.classify_until(lMyUntils, oDataStructure)
    while oDataStructure.is_next_token("|"):
        oDataStructure.replace_next_token_with(token.bar)
        choice.classify_until(lMyUntils, oDataStructure)
