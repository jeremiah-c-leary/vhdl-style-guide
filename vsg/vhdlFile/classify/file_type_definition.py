# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import file_type_definition as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import type_mark


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    file_type_definition ::=
        file of type_mark
    """

    if oDataStructure.is_next_token("file"):
        classify(oDataStructure)
        return True

    return False


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("file", token.file_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_required("of", token.of_keyword, iCurrent, lObjects)

    iCurrent = type_mark.classify(iToken, lObjects)

    return iCurrent
