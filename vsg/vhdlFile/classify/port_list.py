# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import interface_list
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    """
    port_list ::=
        *port*_interface_list
    """

    return interface_list.classify(iToken, lObjects)
