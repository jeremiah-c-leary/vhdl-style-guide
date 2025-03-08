# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import expression
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def classify_until(lUntils, oDataStructure):
    """
    condition ::=
        expression
    """
    expression.classify_until(lUntils, oDataStructure)
