# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import expression


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    """
    generate_specification ::=
        static_discrete_range
      | static_expression
      | alternative_label
    """

    return expression.classify_until([")"], iToken, lObjects)
