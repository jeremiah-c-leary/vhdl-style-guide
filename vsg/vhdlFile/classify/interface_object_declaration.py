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
def detect(oDataStructure):
    """
    interface_object_declaration ::=
        interface_constant_declaration
      | interface_signal_declaration
      | interface_variable_declaration
      | interface_file_declaration
    """

    if interface_constant_declaration.detect(oDataStructure):
        return interface_constant_declaration.classify(oDataStructure)

    if interface_signal_declaration.detect(oDataStructure):
        return interface_signal_declaration.classify(oDataStructure)

    if interface_variable_declaration.detect(oDataStructure):
        return interface_variable_declaration.classify(oDataStructure)

    if interface_file_declaration.detect(oDataStructure):
        return interface_file_declaration.classify(oDataStructure)

    if interface_unknown_declaration.detect(oDataStructure):
        return interface_unknown_declaration.classify(oDataStructure)

    return False
#    iReturn = interface_constant_declaration.detect(iCurrent, lObjects)
#    if iReturn != iCurrent:
#        return iReturn
#
#    iReturn = interface_signal_declaration.detect(iCurrent, lObjects)
#    if iReturn != iCurrent:
#        return iReturn
#
#    iReturn = interface_variable_declaration.detect(iCurrent, lObjects)
#    if iReturn != iCurrent:
#        return iReturn
#
#    iReturn = interface_file_declaration.detect(iCurrent, lObjects)
#    if iReturn != iCurrent:
#        return iReturn
#
#    ### This captures constant, signal and variable declarations without optional keywords
#    ### This is typically done in port lists
#    iReturn = interface_unknown_declaration.detect(iCurrent, lObjects)
#    if iReturn != iCurrent:
#        return iReturn
#
#    return iCurrent
