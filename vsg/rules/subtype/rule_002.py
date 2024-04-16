# -*- coding: utf-8 -*-

from vsg import parser, token
from vsg.rules import consistent_token_case as Rule

lTokens = []
lTokens.append(token.subtype_declaration.identifier)

lNames = []
lNames.append(parser.todo)
lNames.append(token.type_mark.name)


class rule_002(Rule):
    """
    This rule checks for consistent capitalization of subtype names.

    **Violation**

    .. code-block:: vhdl

       subtype read_size is range 0 to 9;
       subtype write_size is range 0 to 9;

       signal read  : READ_SIZE;
       signal write : write_size;

       constant read_sz  : read_size := 8;
       constant write_sz : WRITE_size := 1;


    **Fix**

    .. code-block:: vhdl

       subtype read_size is range 0 to 9;
       subtype write_size is range 0 to 9;

       signal read  : read_size;
       signal write : write_size;

       constant read_sz  : read_size := 8;
       constant write_sz : write_size := 1;
    """

    def __init__(self):
        super().__init__(lTokens, lNames)
        self.bIncludeDeclarativePartNames = True
