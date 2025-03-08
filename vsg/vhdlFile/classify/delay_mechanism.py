# -*- coding: utf-8 -*-

from vsg.token import delay_mechanism as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import expression
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    delay_mechanism ::=
        transport
      | [ reject *time*_expression ] inertial
    """
    if oDataStructure.is_next_token_one_of(["transport", "reject", "inertial"]):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    if utils.is_next_token("transport", iToken, lObjects):
        return utils.assign_next_token_required("transport", token.transport_keyword, iToken, lObjects)

    else:
        iCurrent = iToken

        if utils.is_next_token("reject", iCurrent, lObjects):
            iCurrent = utils.assign_next_token_required("reject", token.reject_keyword, iCurrent, lObjects)
            iCurrent = expression.classify_until(["inertial"], iCurrent, lObjects)

        iCurrent = utils.assign_next_token_required("inertial", token.inertial_keyword, iCurrent, lObjects)
        return iCurrent
