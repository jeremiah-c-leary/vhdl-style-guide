# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import sequential_statement


def detect(oDataStructure):
    """
    process_statement_part ::=
        { sequential_statement }
    """

    while sequential_statement.detect(oDataStructure):
        pass
