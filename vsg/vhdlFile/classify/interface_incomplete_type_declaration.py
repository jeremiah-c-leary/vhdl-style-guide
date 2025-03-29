# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import interface_incomplete_type_declaration as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import identifier


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    interface_incomplete_type_declaration ::=
        type identifier
    """
    return oDataStructure.is_next_token("type")


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with_if("type", token.type_keyword)
    identifier.classify(oDataStructure)
