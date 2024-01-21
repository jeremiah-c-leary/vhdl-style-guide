
from vsg.rules import token_prefix_between_tokens

from vsg import token

lTokens = []
lTokens.append(token.parameter_specification.identifier)


class rule_602(token_prefix_between_tokens):
    '''
    This rule checks for valid prefixes on loop parameter identifiers.
    The default loop prefix is *lv\_*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

      for index in t_range loop

    **Fix**

    .. code-block:: vhdl

      for lv_index in t_range loop
    '''

    def __init__(self):
        token_prefix_between_tokens.__init__(self, 'loop_statement', '602', lTokens, token.iteration_scheme.for_keyword, token.parameter_specification.in_keyword)
        self.prefixes = ['lv_']
