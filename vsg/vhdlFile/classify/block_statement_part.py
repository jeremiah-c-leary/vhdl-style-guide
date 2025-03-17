# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import concurrent_statement


@decorators.print_classifier_debug_info(__name__)
def detect(iToken, lObjects):
    """
    block_statement_part ::=
        { concurrent_statement }
    """

    return utils.detect_submodule(iToken, lObjects, concurrent_statement)
