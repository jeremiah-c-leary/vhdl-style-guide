
from vsg.rules import token_suffix

from vsg import token

lTokens = []
lTokens.append(token.incomplete_type_declaration.identifier)
lTokens.append(token.full_type_declaration.identifier)


class rule_600(token_suffix):
    '''
    This rule checks for valid suffixes in user defined type identifiers.
    The default new type suffix is *\_t*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       type my_type is range -5 to 5 ;

    **Fix**

    .. code-block:: vhdl

       type my_type_t is range -5 to 5 ;
    '''

    def __init__(self):
        token_suffix.__init__(self, 'type', '600', lTokens)
        self.suffixes = ['_t']
        self.solution = 'Type identifiers'
