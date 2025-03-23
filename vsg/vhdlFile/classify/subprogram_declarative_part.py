# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import subprogram_declarative_item


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    subprogram_declarative_part ::=
        { subprogram_declarative_item }
    """

    while subprogram_declarative_item.detect(oDataStructure):
        pass
