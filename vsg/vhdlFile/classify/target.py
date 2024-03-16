# -*- coding: utf-8 -*-

from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import aggregate


def classify(iToken, lObjects, oTokenClass):
    """
    target ::=
        name
      | aggregate
    """
    if utils.is_next_token("(", iToken, lObjects):
        return aggregate.classify(iToken, lObjects, oTokenClass)
    else:
        return utils.assign_tokens_until(":=", oTokenClass.simple_name, iToken, lObjects)
