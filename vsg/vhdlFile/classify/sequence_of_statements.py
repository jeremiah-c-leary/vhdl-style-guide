# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import sequential_statement


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure, lUnless):
    """
    sequence_of_statements ::=
        { sequential_statement }
    """
    while not oDataStructure.is_next_token_one_of(lUnless):
        if not sequential_statement.detect(oDataStructure):
            return False
