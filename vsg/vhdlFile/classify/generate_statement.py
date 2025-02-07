# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import (
    case_generate_statement,
    for_generate_statement,
    if_generate_statement,
)


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
