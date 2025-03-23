# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import expression


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    file_logical_name ::= *string*_expression
    """

    expression.classify_until([";"], oDataStructure)
