# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import package_instantiation_declaration as token
from vsg.vhdlFile.classify import generic_map_aspect, identifier


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    package_instantiation_declaration ::=
        package identifier is new *uninstantiated_package*_name
            [ generic_map_aspect ] ;
    """
    if oDataStructure.are_next_consecutive_tokens(["package", None, "is", "new"]):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_required("package", token.package_keyword)

    identifier.classify(oDataStructure)

    oDataStructure.replace_next_token_required("is", token.is_keyword)
    oDataStructure.replace_next_token_required("new", token.new_keyword)
    oDataStructure.replace_next_token_with(token.uninstantiated_package_name)

    generic_map_aspect.detect(oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
