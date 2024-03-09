
from vsg import parser
from vsg import token

from vsg.rules import consistent_token_case as Rule

lTokens = []
lTokens.append(token.enumeration_type_definition.enumeration_literal)

lNames = []
lNames.append(parser.todo)


class rule_501(Rule):
    '''
    This rule checks for consistent capitalization of enumerated types.

    **Violation**

    .. code-block:: vhdl

       type state is (IDLE, WRITE, READ);

       state <= Idle;
       state <= write;
       state <= ReAd;

    **Fix**

    .. code-block:: vhdl

       type state is (IDLE, WRITE, READ);

       state <= IDLE;
       state <= WRITE;
       state <= READ;
    '''

    def __init__(self):
        Rule.__init__(self, lTokens, lNames)
        self.subphase = 2
        self.bIncludeDeclarativePartNames = True
