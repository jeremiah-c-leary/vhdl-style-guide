# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import array_constraint, range_constraint, record_constraint


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    constraint ::=
        range_constraint
      | array_constraint
      | record_constraint
    """

    oDataStructure.push_seek_index()
    if range_constraint.detect(oDataStructure):
        oDataStructure.pop_seek_index()
        return True

    oDataStructure.pop_seek_index()
    oDataStructure.push_seek_index()
    if array_constraint.detect(oDataStructure):
        oDataStructure.pop_seek_index()
        return True

    oDataStructure.pop_seek_index()
    oDataStructure.push_seek_index()
    if record_constraint.detect(oDataStructure):
        oDataStructure.pop_seek_index()
        return True

    oDataStructure.pop_seek_index()
    oDataStructure.push_seek_index()
    if array_constraint.detect_discrete_subtype_indication(oDataStructure):
        oDataStructure.pop_seek_index()
        return True

    oDataStructure.pop_seek_index()
    return False
