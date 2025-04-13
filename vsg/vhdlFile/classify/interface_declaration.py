# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import (
    interface_object_declaration,
    interface_package_declaration,
    interface_subprogram_declaration,
    interface_type_declaration,
)


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
        interface_object_declaration.classify(oDataStructure)
        return True

    if interface_type_declaration.detect(oDataStructure):
        return True

    if interface_subprogram_declaration.detect(oDataStructure):
        interface_subprogram_declaration.classify(oDataStructure)
        return True

    if interface_package_declaration.detect(oDataStructure):
        interface_package_declaration.classify(oDataStructure)
        return True

    return False
