# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import element_constraint


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    array_element_constraint ::= element_constraint
    """
    return element_constraint.detect(oDataStructure)
