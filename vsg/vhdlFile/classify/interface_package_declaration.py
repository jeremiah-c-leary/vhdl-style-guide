# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import interface_package_declaration as token
from vsg.vhdlFile.classify import identifier, interface_package_generic_map_aspect


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    interface_package_declaration ::=
        package identifier is
            new *uninstantiated_package*_name interface_package_generic_map_aspect
    """
    return oDataStructure.is_next_token("package")


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_required("package", token.package_keyword)

    identifier.classify(oDataStructure)

    oDataStructure.replace_next_token_required("is", token.is_keyword)
    oDataStructure.replace_next_token_required("new", token.new_keyword)
    oDataStructure.replace_next_token_with(token.uninstantiated_package_name)

    interface_package_generic_map_aspect.detect(oDataStructure)
