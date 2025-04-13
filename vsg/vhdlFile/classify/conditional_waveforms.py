# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import conditional_waveforms as token
from vsg.vhdlFile.classify import condition, waveform


@decorators.print_classifier_debug_info(__name__)
def classify_until(lUntils, oDataStructure):
    """
    conditional_waveforms ::=
        waveform when condition
        { else waveform when condition }
        [ else waveform ]
    """

    lMyElseUntils = lUntils.copy()
    lMyElseUntils.append("else")
    lMyWhenUntils = lUntils.copy()
    lMyWhenUntils.append("when")

    waveform.classify_until(["when"], oDataStructure)

    oDataStructure.replace_next_token_required("when", token.when_keyword)

    condition.classify_until(lMyElseUntils, oDataStructure)

    while oDataStructure.is_next_token("else"):
        oDataStructure.replace_next_token_required("else", token.else_keyword)

        waveform.classify_until(lMyWhenUntils, oDataStructure)

        if oDataStructure.is_next_token_one_of(lUntils):
            break

        oDataStructure.replace_next_token_required("when", token.when_keyword)

        condition.classify_until(lMyElseUntils, oDataStructure)
