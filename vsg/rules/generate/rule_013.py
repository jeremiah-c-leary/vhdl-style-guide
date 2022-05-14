
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.case_generate_statement.end_generate_keyword, token.case_generate_statement.end_generate_label])
lTokens.append([token.for_generate_statement.end_generate_keyword, token.for_generate_statement.end_generate_label])
lTokens.append([token.if_generate_statement.end_generate_keyword, token.if_generate_statement.end_generate_label])


class rule_013(Rule):
    '''
    This rule checks for a single space after the **generate** keyword and the label in the **end generate** keywords.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       end generate    ram_array;

    **Fix**

    .. code-block:: vhdl

       end generate ram_array;
    '''
    def __init__(self):
        Rule.__init__(self, 'generate', '013', lTokens)
