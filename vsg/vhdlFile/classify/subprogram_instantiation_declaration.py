# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import subprogram_instantiation_declaration as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import generic_map_aspect, signature, subprogram_kind


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    subprogram_instantiation_declaration ::=
        subprogram_kind identifier is new uninstantiated_subprogram_name [ signature ]
            [ generic_map_aspect ] ;
    """

    if subprogram_kind.detect(oDataStructure):
        if oDataStructure.find_in_next_n_tokens("is", 3):
            if oDataStructure.find_in_next_n_tokens("new", 4):
                classify(oDataStructure)
                return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    iCurrent = subprogram_kind.classify(iToken, lObjects)

    iCurrent = utils.assign_next_token(token.identifier, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required("is", token.is_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required("new", token.new_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token(token.uninstantiated_subprogram_name, iCurrent, lObjects)

    iCurrent = signature.detect(iCurrent, lObjects)

    iCurrent = generic_map_aspect.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent
