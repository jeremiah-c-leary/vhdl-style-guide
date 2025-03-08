# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import constraint, resolution_indication, type_mark
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    subtype_indication ::=
        [ resolution_indication ] type_mark [ constraint ]
    """
    resolution_indication.detect(oDataStructure)

    type_mark.classify(oDataStructure)

    constraint.detect(oDataStructure)
