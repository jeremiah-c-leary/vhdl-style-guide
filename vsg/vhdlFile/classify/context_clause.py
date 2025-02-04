# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import context_item, utils


def detect(oDataStructure):
    """
    context_clause ::=
        { context_item }
    """
    return utils.detect_production(oDataStructure, context_item)
