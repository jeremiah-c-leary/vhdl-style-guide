# -*- coding: utf-8 -*-


from vsg.vhdlFile.classify import full_type_declaration, incomplete_type_declaration


def detect(oDataStructure):
    """
    type_declaration ::=
        full_type_declaration
      | incomplete_type_declaration
    """

    if full_type_declaration.detect(oDataStructure):
        return True

    return incomplete_type_declaration.detect(oDataStructure)
