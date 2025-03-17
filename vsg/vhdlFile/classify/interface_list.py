# -*- coding: utf-8 -*-

from vsg.token import interface_list as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import interface_element
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    interface_list ::=
        interface_element { ; interface_element }
    """

    interface_element.classify(oDataStructure)

    while oDataStructure.is_next_token(";"):
        oDataStructure.replace_next_token_with(token.semicolon)
        interface_element.classify(oDataStructure)
