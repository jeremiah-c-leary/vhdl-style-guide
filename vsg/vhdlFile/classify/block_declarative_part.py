# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import block_declarative_item


@decorators.print_classifier_debug_info(__name__)
def detect(iToken, lObjects):
    """
    block_declarative_part ::=
        { block_declarative_item }
    """

    return utils.detect_submodule(iToken, lObjects, block_declarative_item)
