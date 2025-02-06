# -*- coding: utf-8 -*-

from vsg.token import association_list as token
from vsg.vhdlFile.classify import association_element


def classify(oDataStructure):
    """
    association_list ::=
        association_element { , association_element }
    """
    association_element.detect(oDataStructure)

    while oDataStructure.is_next_token(","):
        oDataStructure.replace_next_token_with(token.comma)
        association_element.detect(oDataStructure)
