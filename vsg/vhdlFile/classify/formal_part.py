# -*- coding: utf-8 -*-

from vsg import parser
from vsg.vhdlFile import utils


def classify(oTokenType, iToken, lObjects):
    """
    formal_part ::=
         formal_designator
      |  function_name ( formal_designator )
      |  type_mark ( formal_designator )

    An association element will end with =>
    """
    # Assign first token as formal part
    iCurrent = utils.assign_next_token(oTokenType, iToken, lObjects)

    # Assign remaining tokens as todo
    while not utils.are_next_consecutive_tokens_ignoring_whitespace(["=>"], iCurrent, lObjects):
        iCurrent = utils.assign_next_token(parser.todo, iCurrent, lObjects)

    return iCurrent
