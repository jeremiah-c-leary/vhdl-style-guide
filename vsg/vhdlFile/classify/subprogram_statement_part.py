# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import sequential_statement


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    subprogram_statement_part ::=
        { sequential_statement }
    """

    while sequential_statement.detect(oDataStructure):
        pass

    return False
