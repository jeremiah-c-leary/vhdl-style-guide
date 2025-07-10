# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import access_type_definition as token
from vsg.vhdlFile.classify import subtype_indication


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    access_type_definition ::=
        access subtype_indication
    """

    if oDataStructure.is_next_token("access"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.access_keyword)

    subtype_indication.classify(oDataStructure)
