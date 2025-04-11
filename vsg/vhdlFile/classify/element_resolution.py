# -*- coding: utf-8 -*-

from vsg import decorators, parser
from vsg.vhdlFile.classify import utils


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    element_resolution ::=
        array_constraint
      | record_constraint
    """

    utils.assign_tokens_until_matching_closing_paren(parser.todo, oDataStructure)
