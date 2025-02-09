# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import sequential_statement


def detect(oDataStructure):
    """
    sequence_of_statements ::=
        { sequential_statement }
    """
    while sequential_statement.detect(oDataStructure):
        pass
