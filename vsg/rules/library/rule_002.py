
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.library_clause.keyword, token.logical_name_list.logical_name])


class rule_002(Rule):
    '''
    This rule checks for excessive spaces after the **library** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       library    ieee;

    **Fix**

    .. code-block:: vhdl

       library ieee;
    '''
    def __init__(self):
        Rule.__init__(self, 'library', '002', lTokens)
