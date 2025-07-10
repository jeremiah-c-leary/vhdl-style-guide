# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import interface_declaration


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    interface_element ::=
        interface_declaration
    """

    interface_declaration.detect(oDataStructure)
