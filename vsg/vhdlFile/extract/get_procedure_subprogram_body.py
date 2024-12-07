# -*- coding: utf-8 -*-

from vsg import token
from vsg.vhdlFile.extract import get_subprogram_body


def get_procedure_subprogram_body(lAllObjects, oTokenMap):
    lToi = get_subprogram_body(lAllObjects, oTokenMap)

    lReturn = []
    for oToi in lToi:
        bSubprogramIsProcedure = oToi.does_first_token_match(token.procedure_specification.procedure_keyword)
        if bSubprogramIsProcedure:
            oToken = oToi.get_first_token_matching(token.procedure_specification.designator)
            oToi.set_token_value(oToken.get_value())
            lReturn.append(oToi)

    return lReturn
