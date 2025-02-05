# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import entity_declarative_item


def detect(oDataStructure):
    """
    entity_declarative_part ::=
        { entity_declarative_item }
    """

    while entity_declarative_item.detect(oDataStructure):
        pass
