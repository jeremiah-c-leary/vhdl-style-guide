# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import package_declarative_item


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    package_declarative_part ::=
        { package_declarative_item }
    """

    while package_declarative_item.detect(oDataStructure):
        pass
