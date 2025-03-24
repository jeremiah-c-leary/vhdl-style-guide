# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import block_declarative_item


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    block_declarative_part ::=
        { block_declarative_item }
    """

    while block_declarative_item.detect(oDataStructure):
        pass
