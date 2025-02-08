# -*- coding: utf-8 -*-

from vsg.token import type_mark as token
from vsg.vhdlFile.classify import attribute_name


def classify(oDataStructure):
    """
    type_mark ::=
        *type*_name
      | *subtype*_name
    """

    if attribute_name.detect(oDataStructure):
        return attribute_name.classify(oDataStructure)

    oDataStructure.replace_next_token_with(token.name)
