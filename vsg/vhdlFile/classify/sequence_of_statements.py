# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import sequential_statement
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    sequence_of_statements ::=
        { sequential_statement }
    """
    while sequential_statement.detect(oDataStructure):
        pass
