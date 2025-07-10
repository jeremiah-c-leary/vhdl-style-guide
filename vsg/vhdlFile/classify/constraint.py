# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import array_constraint, range_constraint, record_constraint


@decorators.print_classifier_debug_info(__name__)
@decorators.push_pop_seek_index
def detect(oDataStructure):
    """
    constraint ::=
        range_constraint
      | array_constraint
      | record_constraint
    """

    if range_constraint.detect(oDataStructure):
        return True

    if array_constraint.detect(oDataStructure):
        return True

    if record_constraint.detect(oDataStructure):
        return True

    return array_constraint.detect_discrete_subtype_indication(oDataStructure)
