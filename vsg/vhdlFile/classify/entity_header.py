# -*- coding: utf-8 -*-


from vsg import decorators
from vsg.vhdlFile.classify import generic_clause, port_clause


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    entity_header ::=
        [ *formal*_generic_clause ]
        [ *formal*_port_clause ]
    """

    bGeneric = False
    if generic_clause.detect(oDataStructure):
        generic_clause.classify(oDataStructure)
        bGeneric = True

    bPort = False
    if port_clause.detect(oDataStructure):
        port_clause.classify(oDataStructure)
        bPort = True

    return bGeneric or bPort
