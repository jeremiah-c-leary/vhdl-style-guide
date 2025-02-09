# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import expression


def classify_until(lUntils, oDataStructure):
    """
    condition ::=
        expression
    """
    expression.classify_until(lUntils, oDataStructure)
