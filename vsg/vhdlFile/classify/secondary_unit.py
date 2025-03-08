# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import architecture_body, package_body
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    secondary_unit ::=
        architecture_body
      | package_body
    """
    if architecture_body.detect(oDataStructure):
        return True

    return package_body.detect(oDataStructure)
