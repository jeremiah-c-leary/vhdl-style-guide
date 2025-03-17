# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import protected_type_body_declarative_item


@decorators.print_classifier_debug_info(__name__)
def detect(iToken, lObjects):
    """
    protected_type_body_declarative_part ::=
        { protected_type_body_declarative_item }
    """

    return utils.detect_submodule(iToken, lObjects, protected_type_body_declarative_item)
