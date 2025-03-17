# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import component_specification as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import instantiation_list


@decorators.print_classifier_debug_info(__name__)
def detect(iToken, lObjects):
    iCurrent = iToken

    while utils.find_in_next_n_tokens(",", 2, iCurrent, lObjects):
        iCurrent = utils.find_next_token(iCurrent, lObjects)
        iCurrent = utils.find_next_token(iCurrent + 1, lObjects)

    if utils.find_in_next_n_tokens(":", 2, iCurrent, lObjects):
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    """
    component_specification ::=
        instantiation_list : component_name
    """

    iCurrent = iToken

    iCurrent = instantiation_list.classify(iToken, lObjects)

    iCurrent = utils.assign_next_token_required(":", token.colon, iCurrent, lObjects)
    iCurrent = utils.assign_next_token(token.component_name, iCurrent, lObjects)

    return iCurrent
