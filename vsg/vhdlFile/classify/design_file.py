# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import design_unit


@decorators.print_classifier_debug_info(__name__)
def tokenize(oDataStructure):
    """
    design_file ::=
        design_unit { design_unit }
    """
    while design_unit.detect(oDataStructure):
        pass
