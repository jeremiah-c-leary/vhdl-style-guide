# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import sequential_statement


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    sequence_of_statements ::=
        { sequential_statement }
    """
    while sequential_statement.detect(oDataStructure):
        pass
