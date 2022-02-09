
from vsg.rules import token_prefix

from vsg import token

lTokens = []
lTokens.append(token.case_generate_statement.generate_label)
lTokens.append(token.case_generate_statement.end_generate_label)
lTokens.append(token.for_generate_statement.generate_label)
lTokens.append(token.for_generate_statement.end_generate_label)
lTokens.append(token.if_generate_statement.generate_label)
lTokens.append(token.if_generate_statement.end_generate_label)


class rule_017(token_prefix):
    '''
    This rule checks for valid prefixes on generate statement labels.
    The default prefix is *gen\_*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       label : case condition generate

    **Fix**

    .. code-block:: vhdl

       gen_label : case condition generate
    '''

    def __init__(self):
        token_prefix.__init__(self, 'generate', '017', lTokens)
        self.prefixes = ['gen_']
