# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import package_body as token
from vsg.vhdlFile.classify import package_body_declarative_part


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    package_body ::=
        package body *package*_simple_name is
            package_body_declarative_part
        end [ package body ] [ *package*_simple_name ] ;
    """

    if oDataStructure.are_next_consecutive_tokens(["package", "body", None, "is"]):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.package_keyword)
    oDataStructure.replace_next_token_required("body", token.body_keyword)
    oDataStructure.replace_next_token_with(token.package_simple_name)
    oDataStructure.replace_next_token_required("is", token.is_keyword)

    package_body_declarative_part.detect(oDataStructure)

    oDataStructure.replace_next_token_required("end", token.end_keyword)

    if oDataStructure.is_next_token("package"):
        oDataStructure.replace_next_token_with(token.end_package_keyword)
        oDataStructure.replace_next_token_required("body", token.end_body_keyword)

    oDataStructure.replace_next_token_with_if_not(";", token.end_package_simple_name)
    oDataStructure.replace_next_token_required(";", token.semicolon)
