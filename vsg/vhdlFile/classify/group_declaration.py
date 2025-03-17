# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import group_declaration as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import group_constituent_list


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    group_declaration ::=
        group identifier : group_template_name ( group_constituent_list ) ;
    """

    if oDataStructure.is_next_token("group"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with("group", token.group_keyword, iToken, lObjects)
    oDataStructure.replace_next_token_with(token.identifier, iCurrent, lObjects)
    oDataStructure.replace_next_token_required(":", token.colon, iCurrent, lObjects)
    oDataStructure.replace_next_token_with(token.group_template_name, iCurrent, lObjects)
    oDataStructure.replace_next_token_required("(", token.open_parenthesis, iCurrent, lObjects)

    group_constituent_list.classify(oDataStructure)

    oDataStructure.replace_next_token_required(")", token.close_parenthesis, iCurrent, lObjects)
    oDataStructure.replace_next_token_required(";", token.semicolon, iCurrent, lObjects)
