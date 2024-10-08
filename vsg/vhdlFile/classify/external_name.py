# -*- coding: utf-8 -*-

from vsg import parser
from vsg.token import direction
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import (
    external_constant_name,
    external_signal_name,
    external_variable_name,
)


def detect(iToken, lObjects):
    """
    external_name ::=
        external_constant_name
      | external_signal_name
      | external_variable_name
    """

    iReturn = external_constant_name.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = external_signal_name.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = external_variable_name.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    return iToken
