# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import (
    interface_object_declaration,
    interface_package_declaration,
    interface_subprogram_declaration,
    interface_type_declaration,
)
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    interface_declaration ::=
        interface_object_declaration
      | interface_type_declaration
      | interface_subprogram_declaration
      | interface_package_declaration
    """

    if interface_object_declaration.detect(oDataStructure):
        return interface_object_declaration.classify(oDataStructure)

    if interface_type_declaration.detect(oDataStructure):
        return interface_type_declaration.classify(oDataStructure)

    if interface_subprogram_declaration.detect(oDataStructure):
        return interface_subprogram_declaration.classify(oDataStructure)

    if interface_package_declaration.detect(oDataStructure):
        return interface_package_declaration.classify(oDataStructure)

    return False
#    iCurrent = interface_object_declaration.detect(iToken, lObjects)
#    if iCurrent != iToken:
#        return iCurrent
#
#    iCurrent = interface_type_declaration.detect(iToken, lObjects)
#    if iCurrent != iToken:
#        return iCurrent
#
#    iCurrent = interface_subprogram_declaration.detect(iToken, lObjects)
#    if iCurrent != iToken:
#        return iCurrent
#
#    iCurrent = interface_package_declaration.detect(iToken, lObjects)
#    if iCurrent != iToken:
#        return iCurrent
#
#    return iToken
