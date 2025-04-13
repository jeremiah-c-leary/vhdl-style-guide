# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import simple_release_assignment as token
from vsg.vhdlFile.classify import force_mode, utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    simple_release_assignment ::=
        target <= release [ force_mode ] ;
    """

    return oDataStructure.does_string_exist_before_string("release", ";")


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    utils.assign_tokens_until("<=", token.target, oDataStructure)
    oDataStructure.replace_next_token_required("<=", token.assignment)
    oDataStructure.replace_next_token_required("release", token.release_keyword)

    force_mode.detect(oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
