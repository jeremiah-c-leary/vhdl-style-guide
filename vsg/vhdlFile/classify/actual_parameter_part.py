# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import association_list


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    actual_parameter_part ::=
        *parameter*_association_list
    """

    association_list.classify(oDataStructure)
