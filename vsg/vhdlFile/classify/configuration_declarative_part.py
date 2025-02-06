# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import configuration_declarative_item


def detect(oDataStructure):
    """
    configuration_declarative_part ::=
        { configuration_declarative_item }
    """

    while configuration_declarative_item.detect(oDataStructure):
        pass
