# -*- coding: utf-8 -*-

from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import block_declarative_item


def detect(oDataStructure):
    """
    architecture_declarative_part ::=
        { block_declarative_item }
    """

    while block_declarative_item.detect(oDataStructure):
        pass
