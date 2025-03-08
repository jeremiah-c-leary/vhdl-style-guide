# -*- coding: utf-8 -*-

from vsg.token import choices as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import choice
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def classify_until(lUntils, iToken, lObjects):
    """
    choices ::=
        choice { | choice }
    """
    iCurrent = iToken
    iLast = 0
    lMyUntils = lUntils
    lMyUntils.append("|")

    while iLast != iCurrent:
        iLast = iCurrent
        iCurrent = choice.classify_until(lMyUntils, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_if("|", token.bar, iCurrent, lObjects)

    return iCurrent
