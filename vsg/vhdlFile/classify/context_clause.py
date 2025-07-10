# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import context_item, utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    context_clause ::=
        { context_item }
    """
    return utils.detect_production(oDataStructure, context_item)
