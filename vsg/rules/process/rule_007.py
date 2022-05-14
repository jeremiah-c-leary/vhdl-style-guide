
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.process_statement.end_keyword, token.process_statement.end_postponed_keyword])
lTokens.append([token.process_statement.end_keyword, token.process_statement.end_process_keyword])


class rule_007(Rule):
    '''
    This rule checks for a single space after the **end** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       end   process proc_a;

    **Fix**

    .. code-block:: vhdl

       end process proc_a;
    '''
    def __init__(self):
        Rule.__init__(self, 'process', '007', lTokens)
