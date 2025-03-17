# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import interface_list


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    """
    formal_parameter_list ::=
        *parameter*_interface_list
    """

    return interface_list.classify(iToken, lObjects)
