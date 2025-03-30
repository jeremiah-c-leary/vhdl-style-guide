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
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.alias_keyword)

    oDataStructure.replace_next_token_with(token.alias_designator)

    if oDataStructure.is_next_token(":"):
        oDataStructure.replace_next_token_with(token.colon)
        subtype_indication.classify(oDataStructure)

    oDataStructure.replace_next_token_required("is", token.is_keyword)

    name.classify_until([";", "["], oDataStructure)

    if signature.detect(oDataStructure):
        signature.classify(oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
