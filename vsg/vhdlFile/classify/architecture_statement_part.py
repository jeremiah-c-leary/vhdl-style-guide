# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import concurrent_statement
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    architecture_statement_part ::=
        { concurrent_statement }
    """

    while concurrent_statement.detect(oDataStructure):
        pass
