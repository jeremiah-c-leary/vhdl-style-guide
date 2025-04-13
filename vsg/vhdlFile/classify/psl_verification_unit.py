# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token.psl import verification_unit as token


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
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

    if oDataStructure.is_next_token_one_of(["vunit", "vpkg", "vprop", "vmode"]):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with_if("vunit", token.vunit_keyword)
    oDataStructure.replace_next_token_with_if("vpkg", token.vpkg_keyword)
    oDataStructure.replace_next_token_with_if("vprop", token.vprop_keyword)
    oDataStructure.replace_next_token_with_if("vmode", token.vmode_keyword)

    while not oDataStructure.is_next_token("{"):
        oDataStructure.replace_next_token_with(token.todo)

    oDataStructure.replace_next_token_required("{", token.open_curly)

    while not oDataStructure.is_next_token("}"):
        oDataStructure.replace_next_token_with(token.todo)

    oDataStructure.replace_next_token_required("}", token.close_curly)
