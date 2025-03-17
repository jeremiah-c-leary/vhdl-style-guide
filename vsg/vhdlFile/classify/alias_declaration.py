# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import alias_declaration as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import name, signature, subtype_indication


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    alias_declaration ::=
        alias alias_designator [ : subtype_indication ] is name [ signature ] ;
    """

    if oDataStructure.is_next_token("alias"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("alias", token.alias_keyword, iToken, lObjects)

    iCurrent = utils.assign_next_token(token.alias_designator, iCurrent, lObjects)

    if utils.is_next_token(":", iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required(":", token.colon, iCurrent, lObjects)
        iCurrent = subtype_indication.classify(iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required("is", token.is_keyword, iCurrent, lObjects)

    iCurrent = name.classify_until([";", "["], iCurrent, lObjects)

    iCurrent = signature.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent
