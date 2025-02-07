# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import package_body_declarative_item


def detect(oDataStructure):
    """
    package_body_declarative_part ::=
        { package_body_declarative_item }
    """

    while package_body_declarative_item.detect(oDataStructure):
        pass
