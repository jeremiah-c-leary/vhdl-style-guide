
from vsg import token

from vsg.vhdlFile.extract import get_subprogram_body


def get_procedure_subprogram_body(lAllObjects, oTokenMap):

    lToi = get_subprogram_body(lAllObjects, oTokenMap)

    lReturn = []
    for oToi in lToi:
        oToken = oToi.get_first_token_matching(token.procedure_specification.procedure_keyword)
        if oToken is not None:
            lReturn.append(oToi)

    return lReturn
