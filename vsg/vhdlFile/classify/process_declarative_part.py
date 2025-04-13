# -*- coding: utf-8 -*-


from vsg import decorators
from vsg.vhdlFile.classify import process_declarative_item


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    process_declarative_part ::=
        { process_declarative_item }
    """

    while process_declarative_item.detect(oDataStructure):
        pass
