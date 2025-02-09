# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import aggregate, utils


def classify(oDataStructure, oTokenClass):
    """
    target ::=
        name
      | aggregate
    """
    if oDataStructure.is_next_token("("):
        aggregate.classify(oDataStructure, oTokenClass)
    else:
        utils.assign_tokens_until(":=", oTokenClass.simple_name, oDataStructure)
