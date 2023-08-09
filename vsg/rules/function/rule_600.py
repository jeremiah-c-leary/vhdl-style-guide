
from vsg.rules import token_prefix

from vsg import token

lTokens = []
lTokens.append(token.function_specification.designator)


class rule_600(token_prefix):
    '''
    This rule checks for valid prefixes on function designators.
    Default signal prefix is *f\_*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       function read_data

    **Fix**

    .. code-block:: vhdl

       function f_read_data
    '''

    def __init__(self):
        token_prefix.__init__(self, 'function', '600', lTokens)
        self.prefixes = ['f_']
        self.solution = 'Function designator'
