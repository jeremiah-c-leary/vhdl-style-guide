# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token.psl import restrict_n_directive as token
from vsg.vhdlFile.classify import utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    [ label : ] Restrict!_Directive

    Assume_Directive ::=
        restrict! Sequence ;
    """

    if oDataStructure.are_next_consecutive_tokens([None, ":", "restrict!"]) or oDataStructure.is_next_token("restrict!"):
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_required("restrict!", token.restrict_n_keyword)

    utils.assign_tokens_until(";", token.todo, oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
