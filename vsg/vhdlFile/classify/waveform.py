# -*- coding: utf-8 -*-

from vsg import decorators, parser
from vsg.token import waveform as token
from vsg.vhdlFile.classify import waveform_element


@decorators.print_classifier_debug_info(__name__)
def classify_until(lUntils, oDataStructure):
    """
    waveform ::=
        waveform_element { , waveform_element }
      | unaffected
    """

    if oDataStructure.is_next_seek_token("unaffected"):
        oDataStructure.replace_next_token_with(token.unaffected_keyword)
    else:
        lMyUntils = lUntils
        lMyUntils.append(",")

        waveform_element.classify_until(lMyUntils, oDataStructure)

        while oDataStructure.is_next_seek_token(","):
            oDataStructure.replace_next_token_with(token.comma)
            waveform_element.classify_until(lMyUntils, oDataStructure)

        oDataStructure.replace_next_token_with_if(")", parser.todo)
