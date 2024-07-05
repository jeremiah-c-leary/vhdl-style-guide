# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import architecture_body, package_body


def detect(iToken, lObjects):
    """
    secondary_unit ::=
        architecture_body
      | package_body
    """
    iReturned = architecture_body.detect(iToken, lObjects)
    if iReturned != iToken:
        return iReturned

    iReturned = package_body.detect(iToken, lObjects)
    if iReturned != iToken:
        return iReturned

    return iToken
