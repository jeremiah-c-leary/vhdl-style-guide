# -*- coding: utf-8 -*-

from vsg.token import entity_designator as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import signature
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    """
    entity_designator ::=
        entity_tag [ signature ]
    """

    iCurrent = utils.assign_next_token(token.entity_tag, iToken, lObjects)

    iCurrent = signature.detect(iCurrent, lObjects)

    return iCurrent
