# -*- coding: utf-8 -*-


from vsg.vhdlFile.classify import process_declarative_item
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    process_declarative_part ::=
        { process_declarative_item }
    """

    while process_declarative_item.detect(oDataStructure):
        pass
