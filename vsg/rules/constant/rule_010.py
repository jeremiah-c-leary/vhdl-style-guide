
from vsg import token

from vsg.rules.whitespace_before_token import Rule

lTokens = []
lTokens.append(token.constant_declaration.assignment_operator)


class rule_010(Rule):
    '''
    This rule checks for a single space before the := keyword in constant declarations.
    Having a space makes it clearer where the assignment occurs on the line.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       constant size : integer:= 1;
       constant width : integer   := 10;

    **Fix**

    .. code-block:: vhdl

       constant size : integer := 1;
       constant width : integer := 10;
    '''
    def __init__(self):
        Rule.__init__(self, 'constant', '010', lTokens)
        self.number_of_spaces = '>=1'
