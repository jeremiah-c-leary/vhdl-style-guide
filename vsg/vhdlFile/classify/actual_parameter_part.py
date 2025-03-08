# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import association_list
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def classify(iTokent, lObjects):
    """
    actual_parameter_part ::=
        *parameter*_association_list
    """

    return association_list.classify(iTokent, lObjects)
