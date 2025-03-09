# -*- coding: utf-8 -*-

from vsg.token.psl import verification_unit as token
from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    """
    psl_verification_unit ::=
        Vunit_Type PSL_Identifier [ ( Context_Spec ) ] **{**
            { Inherit_Spec }
            { Override_Spec }
            { Vunit_Item }
      **}**

    Vunit_Type ::=
        vunit | vpkg | vprop | vmode
    """

    if utils.is_next_token_one_of(["vunit", "vpkg", "vprop", "vmode"], iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_if("vunit", token.vunit_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if("vpkg", token.vpkg_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if("vprop", token.vprop_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if("vmode", token.vmode_keyword, iToken, lObjects)

    while not utils.is_next_token("{", iCurrent, lObjects):
        iCurrent = utils.assign_next_token(token.todo, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required("{", token.open_curly, iCurrent, lObjects)

    while not utils.is_next_token("}", iCurrent, lObjects):
        iCurrent = utils.assign_next_token(token.todo, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required("}", token.close_curly, iCurrent, lObjects)

    return iCurrent
