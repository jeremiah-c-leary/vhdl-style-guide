# -*- coding: utf-8 -*-

from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import constraint, resolution_indication, type_mark


def classify(iToken, lObjects):
    """
    subtype_indication ::=
        [ resolution_indication ] type_mark [ constraint ]
    """

    iCurrent = resolution_indication.detect(iToken, lObjects)
    iCurrent = utils.find_next_non_whitespace_token(iCurrent, lObjects)
    iCurrent = type_mark.classify(iCurrent, lObjects)
    iCurrent = constraint.detect(iCurrent, lObjects)
    return iCurrent
