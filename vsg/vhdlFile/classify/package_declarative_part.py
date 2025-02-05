# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import package_declarative_item


def detect(oDataStructure):
    """
    package_declarative_part ::=
        { package_declarative_item }
    """

    while package_declarative_item.detect(oDataStructure):
        pass
