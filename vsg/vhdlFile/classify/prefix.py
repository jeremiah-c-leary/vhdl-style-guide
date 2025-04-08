# -*- coding: utf-8 -*-

from vsg import decorators, parser
from vsg.vhdlFile.classify import utils


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure, oToken):
    oDataStructure.replace_next_token_with(oToken.name)

    if oDataStructure.is_next_token("("):
        oDataStructure.replace_next_token_with(parser.open_parenthesis)

        utils.assign_tokens_until_matching_closing_paren(parser.todo, oDataStructure)

        oDataStructure.replace_next_token_with(parser.close_parenthesis)
