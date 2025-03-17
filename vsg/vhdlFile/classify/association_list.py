# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import association_list as token
from vsg.vhdlFile.classify import association_element


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    association_list ::=
        association_element { , association_element }
    """
    association_element.detect(oDataStructure)

    while oDataStructure.is_next_token(","):
        oDataStructure.replace_next_token_with(token.comma)
        association_element.detect(oDataStructure)
