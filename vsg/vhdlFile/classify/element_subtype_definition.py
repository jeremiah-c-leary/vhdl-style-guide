# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import subtype_indication


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    element_subtype_definition ::=
        subtype_indication
    """

    subtype_indication.classify(oDataStructure)
