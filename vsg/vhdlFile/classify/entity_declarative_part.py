# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import entity_declarative_item


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    entity_declarative_part ::=
        { entity_declarative_item }
    """

    while entity_declarative_item.detect(oDataStructure):
        pass
