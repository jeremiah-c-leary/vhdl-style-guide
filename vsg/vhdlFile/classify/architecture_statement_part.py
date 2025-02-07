# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import concurrent_statement


def detect(oDataStructure):
    """
    architecture_statement_part ::=
        { concurrent_statement }
    """

    while concurrent_statement.detect(oDataStructure):
        pass
