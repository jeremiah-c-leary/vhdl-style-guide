# -*- coding: utf-8 -*-

from vsg import decorators, parser


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure, oTokenType):
    """
    formal_part ::=
         formal_designator
      |  function_name ( formal_designator )
      |  type_mark ( formal_designator )

    An association element will end with =>
    """
    # Assign first token as formal part
    oDataStructure.replace_next_token_with(oTokenType)

    # Assign remaining tokens as todo
    while not oDataStructure.is_next_token("=>"):
        oDataStructure.replace_next_token_with(parser.todo)
