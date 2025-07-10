# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import protected_type_body_declarative_item


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    protected_type_body_declarative_part ::=
        { protected_type_body_declarative_item }
    """

    while protected_type_body_declarative_item.detect(oDataStructure):
        pass
