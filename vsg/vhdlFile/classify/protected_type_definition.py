# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import protected_type_body, protected_type_declaration


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    protected_type_definition ::=
        protected_type_declaration
      | protected_type_body
    """

    if protected_type_declaration.detect(oDataStructure):
        return True

    if protected_type_body.detect(oDataStructure):
        return True

    return False
