# -*- coding: utf-8 -*-

from vsg.token import mode_view_declaration as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import mode_view_element_definition, subtype_indication


def detect(iToken, lObjects):
    """
    mode_view_declaration ::=
      view identifier of unresolved_record_subtype_indication is
        { mode_view_element_definition }
      end view [ mode_view_simple_name ] ;
    """
    if utils.are_next_consecutive_tokens(["view", None, "of"], iToken, lObjects):
        return classify(iToken, lObjects)

    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("view", token.view_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token(token.identifier, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required("of", token.of_keyword, iCurrent, lObjects)
    iCurrent = subtype_indication.classify(iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required("is", token.is_keyword, iCurrent, lObjects)

    iCurrent = utils.classify_subelement_until("end", mode_view_element_definition, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required("end", token.end_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_required("view", token.end_view_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if_not(";", token.end_view_label, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)
    return iCurrent
