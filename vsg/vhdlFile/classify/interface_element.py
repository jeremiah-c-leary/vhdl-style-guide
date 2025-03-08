# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import interface_declaration
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    """
    interface_element ::=
        interface_declaration
    """

    return interface_declaration.detect(iToken, lObjects)
