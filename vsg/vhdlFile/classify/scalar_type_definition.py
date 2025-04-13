# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import (
    enumeration_type_definition,
    integer_type_definition,
    physical_type_definition,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    scalar_type_definition ::=
        enumeration_type_definition
      | integer_type_definition
      | floating_type_definition
      | physical_type_definition

    NOTE:  floating and physical types are not parsed yet.
           They are very similar to integer types, and will hopefully not be required.
    """

    if physical_type_definition.detect(oDataStructure):
        return True

    if enumeration_type_definition.detect(oDataStructure):
        return True

    return integer_type_definition.detect(oDataStructure)
