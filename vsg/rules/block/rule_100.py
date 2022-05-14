
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.block_statement.block_label, token.block_statement.label_colon])
lTokens.append([token.block_statement.label_colon, token.block_statement.block_keyword])
lTokens.append([token.block_statement.block_keyword, token.block_statement.is_keyword])
lTokens.append([token.block_statement.block_keyword, token.block_statement.guard_open_parenthesis])
lTokens.append([token.block_statement.guard_close_parenthesis, token.block_statement.is_keyword])


class rule_100(Rule):
    '''
    This rule checks for a single space between the following block elements:  label, label colon, **block** keyword, guard open parenthesis, guart close parenthesis, and **is** keywords.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       block_label    :    block    (guard_condition)   is
       block_label  :   block    is

    **Fix**

    .. code-block:: vhdl

       block_label : block (guard_condition) is
       block_label : block is
    '''
    def __init__(self):
        Rule.__init__(self, 'block', '100', lTokens)
