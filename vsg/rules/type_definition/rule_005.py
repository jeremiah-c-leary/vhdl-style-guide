
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.enumeration_type_definition.enumeration_literal)


class rule_005(token_indent):
    '''
    This rule checks the indent of multiline enumerated types.

    **Violation**

    .. code-block:: vhdl

       type state_machine is (
       idle,
         write,
       read,
          done);

    **Fix**

    .. code-block:: vhdl

       type state_machine is (
         idle,
         write,
         read,
         done);
    '''

    def __init__(self):
        token_indent.__init__(self, 'type', '005', lTokens)
        self.solution = 'Ensure proper indentation.'
