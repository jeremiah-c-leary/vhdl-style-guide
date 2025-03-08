# -*- coding: utf-8 -*-

from vsg.token import concurrent_procedure_call_statement as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import procedure_call
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    concurrent_procedure_call_statement ::=
        [ label : ] [ postponed ] procedure_call ;
    """
    if procedure_call.detect(oDataStructure):
        iCurrent = utils.tokenize_label(iToken, lObjects, token.label_name, token.label_colon)
        iCurrent = utils.tokenize_postponed(iCurrent, lObjects, token.postponed_keyword)
        iCurrent = procedure_call.classify(iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)
        return True

    return False
