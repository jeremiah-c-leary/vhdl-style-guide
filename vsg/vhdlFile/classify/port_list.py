# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import interface_list


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    port_list ::=
        *port*_interface_list
    """

    interface_list.classify(oDataStructure)
