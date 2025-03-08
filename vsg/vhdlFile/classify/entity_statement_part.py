# -*- coding: utf-8 -*-

from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import entity_statement
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(iToken, lObjects):
    """
    entity_statement_part ::=
        { entity_statement }
    """

    return utils.detect_submodule(iToken, lObjects, entity_statement)
