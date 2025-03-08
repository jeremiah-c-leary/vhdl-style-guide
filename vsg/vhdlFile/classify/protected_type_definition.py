# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import protected_type_body, protected_type_declaration
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(iToken, lObjects):
    """
    protected_type_definition ::=
        protected_type_declaration
      | protected_type_body
    """

    iReturn = protected_type_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = protected_type_body.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    return iToken
