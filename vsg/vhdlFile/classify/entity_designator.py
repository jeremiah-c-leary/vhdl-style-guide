# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import entity_designator as token
from vsg.vhdlFile.classify import signature


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    entity_designator ::=
        entity_tag [ signature ]
    """

    oDataStructure.replace_next_token_with(token.entity_tag)

    if signature.detect(oDataStructure):
        signature.classify(oDataStructure)
