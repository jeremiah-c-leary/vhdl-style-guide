# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import subprogram_declarative_item


@decorators.print_classifier_debug_info(__name__)
def detect(iToken, lObjects):
    """
    subprogram_declarative_part ::=
        { subprogram_declarative_item }
    """

    iLast = 0
    iCurrent = iToken
    while iLast != iCurrent:
        iLast = iCurrent
        iCurrent = subprogram_declarative_item.detect(iCurrent, lObjects)
    return iCurrent
