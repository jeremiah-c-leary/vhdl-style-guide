# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import attribute_specification, group_declaration, use_clause


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    configuration_declarative_item ::=
        use_clause
      | attribute_specification
      | group_declaration
    """

    if use_clause.detect(oDataStructure):
        return True

    if attribute_specification.detect(oDataStructure):
        return True

    return group_declaration.detect(oDataStructure)
