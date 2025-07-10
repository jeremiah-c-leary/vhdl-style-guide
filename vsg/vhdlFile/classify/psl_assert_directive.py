# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token.psl import assert_directive as token
from vsg.vhdlFile.classify import utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    [ label : ] Assert_Directive

    Assert_Directive ::=
        assert Property [ report String ] ;
    """

    if oDataStructure.are_next_consecutive_tokens([None, ":", "assert"]) or oDataStructure.is_next_token("assert"):
        if oDataStructure.does_string_exist_before_string("[", ";") and oDataStructure.does_string_exist_before_string("report", ";"):
            return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_required("assert", token.assert_keyword)

    utils.assign_tokens_until(";", token.todo, oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
