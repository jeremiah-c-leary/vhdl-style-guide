# -*- coding: utf-8 -*-

from vsg import parser
from vsg.vhdlFile.classify import utils
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure, oToken):
    oDataStructure.replace_next_token_with(oToken.name)

    if oDataStructure.is_next_seek_token("("):
        oDataStructure.replace_next_token_with(open_parenthesis)
        utils.replace_tokens_until_matching_closing_paren(parser.todo, oDataStructure)
        oDataStructure.replace_next_token_with(lObjects, iCurrent, parser.close_parenthesis)
