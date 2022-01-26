
from vsg import token

from vsg.rules import whitespace_before_token

lTokens = []
lTokens.append(token.constant_declaration.assignment_operator)


class rule_010(whitespace_before_token):
    '''
    This rule checks for a single space before the := keyword in constant declarations.
    Having a space makes it clearer where the assignment occurs on the line.

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
        whitespace_before_token.__init__(self, 'constant', '010', lTokens)
        self.solution = 'Ensure at least one space before :=.'
