# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import design_unit


def tokenize(oDataStructure):
    """
    design_file ::=
        design_unit { design_unit }
    """
    while design_unit.detect(oDataStructure):
        pass
