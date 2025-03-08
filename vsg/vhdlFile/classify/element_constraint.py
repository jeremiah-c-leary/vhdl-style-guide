# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import array_constraint, record_constraint
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    element_constraint ::=
        array_constraint
      | record_constraint
    """

    if array_constraint.detect(oDataStructure):
        return True

    return record_constraint.detect(oDataStructure)
