# -*- coding: utf-8 -*-

from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import entity_statement
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    entity_statement_part ::=
        { entity_statement }
    """

    while entity_statement.detect(oDataStructure):
        pass

    return False
