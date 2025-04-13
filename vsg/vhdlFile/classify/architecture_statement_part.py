# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import concurrent_statement


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    architecture_statement_part ::=
        { concurrent_statement }
    """

    while concurrent_statement.detect(oDataStructure):
        pass
