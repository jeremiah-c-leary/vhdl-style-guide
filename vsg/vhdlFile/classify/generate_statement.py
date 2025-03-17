# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import (
    case_generate_statement,
    for_generate_statement,
    if_generate_statement,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    generate_statement ::=
        for_generate_statement
      | if_generate_statement
      | case_generate_statement
    """

    if for_generate_statement.detect(oDataStructure):
        return True

    if if_generate_statement.detect(oDataStructure):
        return True

    return case_generate_statement.detect(oDataStructure)
