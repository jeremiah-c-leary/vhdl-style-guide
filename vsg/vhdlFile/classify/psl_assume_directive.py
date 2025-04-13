# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token.psl import assume_directive as token
from vsg.vhdlFile.classify import utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    [ label : ] Assume_Directive

    Assume_Directive ::=
        assume Property ;
    """

    if oDataStructure.are_next_consecutive_tokens([None, ":", "assume"]) or oDataStructure.is_next_token("assume"):
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_required("assume", token.assume_keyword)
    utils.assign_tokens_until(";", token.todo, oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
