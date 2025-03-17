# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import subtype_indication


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    """
    element_subtype_definition ::=
        subtype_indication
    """

    return subtype_indication.classify(iToken, lObjects)
