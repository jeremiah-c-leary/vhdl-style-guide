# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import expression
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    """
    file_logical_name ::= *string*_expression
    """

    iCurrent = expression.classify_until([";"], iToken, lObjects)

    return iCurrent
