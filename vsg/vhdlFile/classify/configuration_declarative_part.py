# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import configuration_declarative_item
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    configuration_declarative_part ::=
        { configuration_declarative_item }
    """

    while configuration_declarative_item.detect(oDataStructure):
        pass
