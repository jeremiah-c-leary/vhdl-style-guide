# -*- coding: utf-8 -*-

from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import concurrent_statement
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(iToken, lObjects):
    """
    block_statement_part ::=
        { concurrent_statement }
    """

    return utils.detect_submodule(iToken, lObjects, concurrent_statement)
