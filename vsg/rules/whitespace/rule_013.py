
from vsg import token

from vsg.rules import n_spaces_before_and_after_tokens

lTokens = []
lTokens.append(token.logical_operator.logical_operator)


class rule_013(n_spaces_before_and_after_tokens):
    '''
    This rule checks for at least a single space before and after logical operators.

    **Violation**

    .. code-block:: vhdl

      if (a = '1')and(b = '0')
      if (a = '0')or (b = '1')

    **Fix**

    .. code-block:: vhdl

      if (a = '1') and (b = '0')
      if (a = '0') or (b = '1')
    '''

    def __init__(self):
        n_spaces_before_and_after_tokens.__init__(self, 'whitespace', '013', 1, lTokens, bNIsMinimum=True)
        self.solution = 'Ensure a single space before and after concat operator.'
