# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token.psl import cover_directive as token
from vsg.vhdlFile.classify import utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    [ label : ] Cover_Directive

    Cover_Directive ::=
        cover Sequence [ report String ] ;
    """

    if oDataStructure.are_next_consecutive_tokens([None, ":", "cover"]) or oDataStructure.is_next_token("cover"):
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_required("cover", token.cover_keyword)
    utils.assign_tokens_until(";", token.todo, oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
