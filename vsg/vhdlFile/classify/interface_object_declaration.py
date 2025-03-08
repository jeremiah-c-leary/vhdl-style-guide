# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import (
    interface_constant_declaration,
    interface_file_declaration,
    interface_signal_declaration,
    interface_unknown_declaration,
    interface_variable_declaration,
)
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(iCurrent, lObjects):
    """
    interface_object_declaration ::=
        interface_constant_declaration
      | interface_signal_declaration
      | interface_variable_declaration
      | interface_file_declaration
    """

    iReturn = interface_constant_declaration.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    iReturn = interface_signal_declaration.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    iReturn = interface_variable_declaration.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    iReturn = interface_file_declaration.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    ### This captures constant, signal and variable declarations without optional keywords
    ### This is typically done in port lists
    iReturn = interface_unknown_declaration.detect(iCurrent, lObjects)
    if iReturn != iCurrent:
        return iReturn

    return iCurrent
