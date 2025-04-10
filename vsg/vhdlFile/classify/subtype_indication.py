# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import constraint, resolution_indication, type_mark


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    subtype_indication ::=
        [ resolution_indication ] type_mark [ constraint ]
    """
    oDataStructure.push_seek_index()
    resolution_indication.detect(oDataStructure)

    oDataStructure.pop_seek_index()
    oDataStructure.push_seek_index()
    type_mark.classify(oDataStructure)

    oDataStructure.pop_seek_index()
    oDataStructure.push_seek_index()
    constraint.detect(oDataStructure)
    oDataStructure.pop_seek_index()
