# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import expression


def classify_until(lUntils, iToken, lObjects):
    """
    choice ::=
        simple_expression
      | discrete_range
      | *element*_simple_name
      | **others**
    """
    iToken = expression.classify_until(lUntils, iToken, lObjects)
    return iToken
