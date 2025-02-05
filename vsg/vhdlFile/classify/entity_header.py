# -*- coding: utf-8 -*-


from vsg.vhdlFile.classify import generic_clause, port_clause


def detect(oDataStructure):
    """
    entity_header ::=
        [ *formal*_generic_clause ]
        [ *formal*_port_clause ]
    """

    generic_clause.detect(oDataStructure)

    port_clause.detect(oDataStructure)
