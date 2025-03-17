# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import package_declaration as token
from vsg.vhdlFile.classify import package_declarative_part, package_header


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    package_declaration ::=
        package identifier is
            package_header
            package_declarative_part
        end [ package ] [ package_simple_name ] ;
    """

    if oDataStructure.is_next_token("package"):
        if not oDataStructure.does_string_exist_in_next_n_tokens("body", 5):
            if not oDataStructure.does_string_exist_in_next_n_tokens("new", 5):
                classify(oDataStructure)
                return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.package_keyword)
    oDataStructure.replace_next_token_with(token.identifier)
    oDataStructure.replace_next_token_required("is", token.is_keyword)

    package_header.detect(oDataStructure)

    package_declarative_part.detect(oDataStructure)

    oDataStructure.replace_next_token_required("end", token.end_keyword)
    oDataStructure.replace_next_token_with_if("package", token.end_package_keyword)
    oDataStructure.replace_next_token_with_if_not(";", token.end_package_simple_name)
    oDataStructure.replace_next_token_required(";", token.semicolon)
