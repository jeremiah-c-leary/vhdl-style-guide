# -*- coding: utf-8 -*-

from vsg.token import attribute_specification as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import entity_specification, expression
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    attribute_specification ::=
        attribute attribute_designator of entity_specification is expression ;
    """
    if oDataStructure.are_next_consecutive_tokens(["attribute", None, "of"]):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("attribute", token.attribute_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token(token.attribute_designator, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required("of", token.of_keyword, iCurrent, lObjects)

    iCurrent = entity_specification.classify(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required("is", token.is_keyword, iCurrent, lObjects)

    iCurrent = expression.classify_until([";"], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent
