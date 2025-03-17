# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import interface_incomplete_type_declaration
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    interface_type_declaration ::=
        interface_incomplete_type_declaration
    """

    if interface_incomplete_type_declaration.detect(oDataStructure):
        return interface_incomplete_type_declaration.classify(oDataStructure)

    return False
