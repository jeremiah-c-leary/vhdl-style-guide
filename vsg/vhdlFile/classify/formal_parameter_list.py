# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import interface_list


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    formal_parameter_list ::=
        *parameter*_interface_list
    """

    interface_list.classify(oDataStructure)
