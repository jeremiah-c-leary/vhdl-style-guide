# -*- coding: utf-8 -*-

from vsg import decorators, parser
from vsg.token import selected_waveforms as token
from vsg.vhdlFile.classify import choices, waveform


@decorators.print_classifier_debug_info(__name__)
def classify_until(lUntils, oDataStructure):
    """
    selected_waveforms ::=
        { waveform when choices , }
        waveform when choices
    """
    lMyUntils = lUntils
    lMyUntils.append(",")

    waveform.classify_until(["when"], oDataStructure)

    oDataStructure.replace_next_token_required("when", token.when_keyword)

    choices.classify_until(lMyUntils, oDataStructure)

    while oDataStructure.is_next_token(","):
        oDataStructure.replace_next_token_with(token.comma)

        waveform.classify_until(["when"], oDataStructure)

        oDataStructure.replace_next_token_required("when", token.when_keyword)

        choices.classify_until(lMyUntils, oDataStructure)
