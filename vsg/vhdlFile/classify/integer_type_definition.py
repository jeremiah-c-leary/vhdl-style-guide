# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import range_constraint


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    integer_type_definition ::=
        range_constraint
    """

    range_constraint.detect(oDataStructure)
