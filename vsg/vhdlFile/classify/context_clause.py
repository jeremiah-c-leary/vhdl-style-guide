# -*- coding: utf-8 -*-

from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import context_item


def detect(oDesignFile):
    """
    context_clause ::=
        { context_item }
    """
    return utils.detect_production(oDesignFile, context_item)
