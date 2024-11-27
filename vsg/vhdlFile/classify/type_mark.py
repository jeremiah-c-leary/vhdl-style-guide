# -*- coding: utf-8 -*-

from vsg import parser
from vsg.token import type_mark as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import attribute_name


def classify(iToken, lObjects):
    """
    type_mark ::=
        *type*_name
      | *subtype*_name
    """

    if attribute_name.detect(iToken, lObjects):
        return attribute_name.classify(iToken, lObjects)

    iCurrent = utils.assign_next_token(token.name, iToken, lObjects)

    return iCurrent
